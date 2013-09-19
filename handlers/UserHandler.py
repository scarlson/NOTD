from handlers.BaseHandler import BaseHandler
from models.User import User
import tornado.web
import datetime
import re
email_reg = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"


class AccountHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, errors=None):
        try:
                q = "Anti-spam timeout, try again in " + \
                    str(self.request.arguments['e'][0]).lower() + \
                    " seconds."
        except:
            q = None
        errors = errors or q
        data = {}
        data['user'] = self.get_current_user()
        data['user'].db_refresh()
        data['email'] = Email(data['user'].user_id)
        data['errors'] = errors
        if not data['user']:
            self.redir()
        else:
            data['subs'] = self.get_current_user_subs()
            data['calendar'] = Calendar(data['subs']).cals
            #self.render("data_check.html", data=data)
            self.render("profile.html", **data)

    def post(self):
        data = {}
        data['errors'] = []
        data['user'] = self.get_current_user()
        try:
            data['name'] = self.request.arguments['name'][0]
        except:
            data['name'] = None
        try:
            data['email'] = self.request.arguments['email'][0]
        except:
            data['email'] = None
        try:
            data['notis'] = self.request.arguments['notis'][0]
        except:
            data['notis'] = None
            
        #self.render('data_check.html',data=data)
        if data['name']:
            data['user'].real_name = data['name']

        if data['email']:
            if (len(data['email']) < 7 or
            re.match(email_reg, data['email']) == None):
                data['errors'].append('Invalid email.')

        if data['notis']:
            if data['notis'] == 'on':
                data['user'].notifications = 'email'
        else:
            data['user'].notifications = None

        emails = None
        if not data['errors']:
            #make sure data is valid before we make db requests
            cur = self.db.cursor()
            if data['email'] and data['email'] != data['user'].email:
                query = """select distinct * from users where lower(email)
                        LIKE %s;"""
                query = cur.mogrify(query, (data['email'].lower(),))
                cur.execute(query)
                emails = cur.fetchall()
                if emails:
                    data['errors'].append('Email already exists.')

        if not data['errors']:
            if data['user'].save():
                self.set_secure_cookie('user', data['user'].pickle)
                if data['email'] and data['email'] != data['user'].email:
                    #this code needs to get the verification under way
                    ## User changed email address, add new email to Email table and send accept hash
                    em = Email(data['user'].user_id)
                    em.email = data['email']
                    if em.save():
                        self.redirect('/user/email/validate')
                    else:
                        data['errors'].append("Email validation dun goofed.")
                else:
                    self.redirect('/account')
            else:
                data['errors'].append("There was an error saving your updates, please try again.")
        self.get(data['errors'])


class EmailValidateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #send emails to the user with the hash
        from models.Email import Email
        user = self.get_current_user()
        em = Email(user.user_id)
        if em.validate():
            self.redirect('/account')
        else:
            data = {}
            now = datetime.datetime.now()
            expire = em.time + datetime.timedelta(minutes=5)
            delta = expire - now
            delta = delta.seconds
            if expire > now:
                data['errors'] = delta
            else:
                data['errors'] = None
            self.redirect('/account?e='+str(data['errors']))


class EmailSubHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, hashsub):
        #user clicked validate link in email
        #move email from email table to users table
        #delete email table entry
        data = {}
        from models.Email import Email
        em = Email(hash_sub=hashsub)
        data['user'] = User(em.user_id)
        data['user'].email = em.email
        if data['user'].save() and em.delete():
            self.set_secure_cookie('user', unicode(data['user'].user_id))
            self.redirect('/account')
        else:
            data['errors'] = "Email validation failed."
            self.redirect('/account?e=' + str(data['errors']))


class EmailUnsubHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        #user clicked unsubscribe in email link, de-notification them
        pass


class CalendarHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        data = {}
        data['user'] = self.get_current_user()
        if not data['user']:
            self.redir()
        else:
            data['subs'] = self.get_current_user_subs()
            data['calendar'] = Calendar(data['subs']).cals
            data['today'] = datetime.date.today()
            #self.render("data_check.html", data=data)
            self.render("calendar.html", **data)

