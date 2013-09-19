from handlers.BaseHandler import BaseHandler
from models.Notd import Board
import json
import random


class IndexHandler(BaseHandler):
    def get(self):
        data = {}
        self.render("index.html", **data)
 
    def unique_hash(self):
        _hashpool = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        _hash = "".join(random.choice(_hashpool) for i in range(8))
        existing = []
        for key in self.data['rooms']:
            existing.append(key)
        if _hash in existing:
            return self.unique_hash()
        return _hash
   
    def _notd(self):
        try:
            _height = int(self.request.arguments['height'][0])
        except:
            _height = 11
        try:
            _width = int(self.request.arguments['width'][0])
        except:
            _width = 12
        
        _height = 25
        _width = 25

        _hash = self.unique_hash()
        self.data['rooms'][_hash] = {}
        self.data['rooms'][_hash]['game'] = Board(width=_width,height=_height)
        self.redirect(_hash)

    def post(self):
        try:
            _game = self.request.arguments['game'][0]
        except:
            _game= None
        if _game == "notd":
            self._notd()
        else:
            self.redirect('/')
