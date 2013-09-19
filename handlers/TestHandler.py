from handlers.BaseHandler import BaseHandler

class TestHandler(BaseHandler):
    def get(self):
        data = {}
        data['user'] = self.get_current_user().__dict__
        self.render('data_check.html',data=data)
