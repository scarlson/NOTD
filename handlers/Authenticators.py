import tornado.web
import tornado.auth
import cPickle as pickle
from models.User import User
from handlers.BaseHandler import BaseHandler


class LoginHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self, errors=None):
        data = {}
        data['user'] = self.get_current_user()
        data['errors'] = errors
        if data['user']:
            self.redir()
        else:
            self.render('login.html', **data)


class FacebookHandler(BaseHandler, tornado.auth.FacebookGraphMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("code", False):
            self.get_authenticated_user(
              redirect_uri='http://noti.tv/login/facebook',
              client_id=self.settings["facebook_api_key"],
              client_secret=self.settings["facebook_secret"],
              code=self.get_argument("code"),
              callback=self.async_callback(self._on_auth),
              extra_fields=['email','username'])
            return
        self.authorize_redirect(redirect_uri='http://noti.tv/login/facebook',
                                client_id=self.settings["facebook_api_key"],
                                extra_params={"scope": "email"})

    def _on_auth(self, user):
        #self.render("data_check.html",data=user)
        if not user:
            raise tornado.web.HTTPError(500, "Facebook auth failed")
        _user = User(real_name=user['name'], email=user['email'],
                facebook=str(user['id']), source='facebook')

        if _user.exists:
            if _user.db_refresh():
                self.set_secure_cookie('user', unicode(_user.user_id))
            self.redir()
        else:
            data = {}
            data['user'] = None
            data['login'] = user
            data['source'] = 'facebook'
            self.set_secure_cookie('login', pickle.dumps(user))
            #self.render('data_check.html',data=user)
            self.render("welcome.html", **data)


class GoogleHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if not self.get_current_user():
            if self.get_argument('openid.mode', None):
                self.get_authenticated_user(self.async_callback(self._on_auth))
                return
            self.authenticate_redirect()
        else:
            self.redir()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, 'Google auth failed')
        try:
            user['google'] = user['username']
        except:
            user['google'] = user['email']
        _user = User(real_name=user['name'], email=user['email'],
                google=user['google'], source='google')
        
        if _user.exists:
            if _user.db_refresh():
                self.set_secure_cookie('user', unicode(_user.user_id))
            self.redir()
        else:
            data = {}
            data['user'] = None
            data['login'] = user
            data['source'] = 'google'
            self.set_secure_cookie('login', pickle.dumps(user))
            self.render("welcome.html", **data)


class TwitterHandler(BaseHandler, tornado.auth.TwitterMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("oauth_token", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Twitter auth failed")
        _user = User(real_name=user['name'],
        username='@' + str(user['username']), twitter=user['id_str'],
        source='twitter')
        
        if _user.exists:
            if _user.db_refresh():
                self.set_secure_cookie('user', unicode(_user.user_id))
            self.redir()
        else:
            data = {}
            data['user'] = None
            data['login'] = user
            data['source'] = 'twitter'
            self.set_secure_cookie('login', pickle.dumps(user))
            self.render("welcome.html", **data)


class LogoutHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        if self.get_current_user():
            self.clear_cookie('user')
        self.redir()
