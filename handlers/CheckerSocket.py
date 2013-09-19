import tornado.websocket
import json
import logging
from models.Board import Board


class WSHandler(tornado.websocket.WebSocketHandler):
    def initialize(self,data=None):
        self.data=data

    def open(self):
        try:
            self.data['users'].add(self)
        except KeyError:
            self.data['users'] = set()
            self.data['users'].add(self)

    def on_message(self,message):
        msg = json.loads(message)
        orig = tuple(map(int, msg['origin'].split('x')))
        targ = tuple(map(int, msg['target'].split('x')))
        #self.write_message(unicode(orig + targ))
        b = self.data['board']
        color = self.data['player']
        q = None
        c = None
        if b.movePiece(orig,targ,color):
            if self.data['player'] == "Red":
                self.data['player'] = "Black"
            else:
                self.data['player'] = "Red"
        self.data['board'] = b
        data = {}
        if b.winner():
            data['result'] = b.winner() + " wins!"
            self.data['board'] = Board()
        else:
            data['result'] = None
        message = json.dumps(data)
        
        for user in self.data['users']:
            try:
                user.write_message(message)
            except:
                pass

    def on_close(self):
        self.data['users'].remove(self)

