from handlers.BaseHandler import BaseHandler
from models.User import User
import tornado.web
import base64
import os
import re

aws_acc_id = ''
aws_secret = '+rwgXOEl9fZ8AO47lHjCNf'
email_reg = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"


class RegisterHandler(BaseHandler):
    def get(self, errors=None):
        data = {}
        data['user'] = self.get_current_user()
        data['errors'] = errors
        if data['user']:
            self.redir()
        else:
            self.render("register.html", **data)

    def post(self):
        try:
            _username = self.request.arguments['username'][0]
        except:
            _username = None
        try:
            _email = self.request.arguments['email'][0]
        except:
            _email = None
        try:
            _password = self.request.arguments['password'][0]
        except:
            _password = None
        try:
            _verify = self.request.arguments['verify'][0]
        except:
            _verify = None
        emails = None
        usernames = None
        data = {}
        data['username'] = _username
        data['email'] = _email
        data['password'] = _password
        data['verify'] = _verify
        data['errors'] = []

        if not data['username'] or not data['password'] or not data['verify']:
            data['errors'].append('Missing field.')

        if data['username'] and len(data['username']) < 4:
            data['errors'].append('Username is too short.')

        if data['verify'] != data['password']:
            data['errors'].append('Passwords do not match.')

        if data['password'] and len(data['password']) < 4:
            data['errors'].append('Password is too short.')

        if data['email']:
            if (len(data['email']) < 7 or
            re.match(email_reg, data['email']) == None):
                data['errors'].append('Invalid email.')

        if not data['errors']:
            #make sure data is valid before we make db requests
            cur = self.db.cursor()
            query = """select distinct * from users where lower(username)
                        LIKE %s and source='local';"""
            query = cur.mogrify(query, (data['username'].lower(),))
            cur.execute(query)
            usernames = cur.fetchall()
            if data['email']:
                query = """select distinct * from users where lower(email)
                        LIKE %s and source='local';"""
                query = cur.mogrify(query, (data['email'].lower(),))
                cur.execute(query)
                emails = cur.fetchall()

        if emails:
            data['errors'].append('Email already exists.')

        if usernames:
            data['errors'].append('Username already exists.')

        if not data['errors']:
            #valid data, save it up
            user = User(username=data['username'], source='local')
            user.set_password(password=data['password'])
            em = Email(user.user_id,data['email'])
            if em.save():
                em.validate()
            self.set_secure_cookie('user', user.pickle)
            self.redirect('/account')
        else:
            self.get(data['errors'])
            data['errors'].append('Missing field.')


class ResetHandler(BaseHandler):
    def get(self):
        data = {}
        data['user'] = self.get_current_user()
        self.render('reset.html', **data)

    def post(self):
        _user = self.get_current_user()
        if not _user:
            email = self.request.arguments['email'][0]
            derp = AmazonSes(aws_acc_id, aws_secret)
            _user = User()
            if _user.load_by_email(email):
                new_pass = base64.urlsafe_b64encode(os.urandom(10))[:10]
                _user.set_password(new_pass)
                text = """A new Noti.tv password was requested for this email.
                        Your new password is \n\n%s""" % new_pass
                derp.send_mail(
                'no-reply@noti.tv',
                'Noti.tv password reset request',
                text,
                ['no-reply@noti.tv'],  # [user.email]
                email_format="text"
                )
        self.redirect('/login')


class PassChangeHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        _user = self.get_current_user()
        old_pass = self.request.arguments['oldpass'][0]
        new_pass = self.request.arguments['newpass'][0]
        verify = self.request.arguments['verify'][0]
        if _user.check_password(old_pass) and new_pass == verify:
            _user.set_password(new_pass)
        self.redirect('/account')


class DeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        _user = self.get_current_user()
        _user.delete()
        self.clear_cookie('user')
        self.redirect('/')
