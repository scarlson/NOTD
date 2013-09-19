import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self,data=None):
        self.data=data

    def player(self):
        if self.get_cookie('notd'):
            return json.loads(self.get_secure_cookie("notd"))
        return None

    def set_player(self, gg):
        gg = json.dumps(gg)
        self.set_secure_cookie('notd', gg)
