import tornado.websocket
import tornado.escape
import json
import copy


class WSHandler(tornado.websocket.WebSocketHandler):
    def initialize(self, data=None):
        self.data = data

    @property
    def player(self):
        p = None
        if self.get_secure_cookie('gg'):
            p = json.loads(self.get_secure_cookie("gg"))
        return p

    def _broadcast(self, room, message):
        for user in self.data['rooms'][room]['users']:
            try:
                user.write_message(message)
            except:
                pass

    def _send(self, room, target, message):
        for user in self.data['rooms'][room]['users']:
            if user.player['player'] == target:
                try:
                    user.write_message(message)
                except:
                    pass

    def open(self):
        pass

    def on_close(self):
        pass

    def on_message(self, message):
        msg = json.loads(message)
        if 'open' in msg:
            try:
                if self.player:
                    self.data['rooms'][msg['open']]['users'].add(self)
            except KeyError:
                self.data['rooms'][msg['open']]['users'] = set()
                self.data['rooms'][msg['open']]['users'].add(self)
            data = {}
            data['player'] = "System"
            data['hex'] = "#4099FF"
            data['text'] = "Spectator"
            if self.player and self.player['room'] == msg['open']:
                data['text'] = self.player['player']
            data['text'] += " has joined."
            data["text"] = tornado.escape.to_basestring(self.render_string('msg.html', **data))
            message = json.dumps(data)
            self._broadcast(msg['open'], message)
        elif 'close' in msg:
            self.data['rooms'][msg['close']]['users'].remove(self)
            data = {}
            data['player'] = "System"
            data['hex'] = "#4099FF"
            data['text'] = "Spectator"
            if self.player and self.player['room'] == msg['close']:
                data['text'] = self.player['player']
            data['text'] += " has left."
            data["text"] = tornado.escape.to_basestring(self.render_string('msg.html', **data))
            message = json.dumps(data)
            self._broadcast(msg['close'], message)
        elif 'chat' in msg:
            data = {}
            data['player'] = "Spectator"
            data['hex'] = "#F8F8F8"
            if self.player and self.player['room'] == msg['room']:
                data['player'] = self.player['player']
            data['text'] = msg['chat']
            data["text"] = tornado.escape.to_basestring(self.render_string('msg.html', **data))
            message = json.dumps(data)
            self._broadcast(msg['room'], message)
        elif 'key' in msg:
            data = self._notd(msg)
            for pc in data:
                self._send(msg['room'], pc, data[pc])
        else:
            pass

    def _notd(self, msg):
        data = {}
        board = self.data['rooms'][msg['room']]['game']
        _player = self.player['player']
        item = None
        target = None
        if 'item' in msg:
            item = msg['item']
        if 'target' in msg:
            target = msg['target']
        board.action(_player, msg['key'], item, target)
        if board.players:
            for pc in board.players:
                data[pc.name] = {}
                npcs = []
                fov = board.fov(pc)
                fom = [copy.copy(f) for f in fov]
                fov = []
                for f in fom:
                    if f.item:
                        f.item.owner = None
                        f.item = f.item.__dict__
                    if f.char and f.char != pc:
                        npc = f.char
                        di = {'x': npc.coords[0], 'y': npc.coords[1], 'facing': npc.facing,
                              'name': npc.name, 'uid': npc.uid, 'health': npc.cur_hp}
                        npcs.append(di)
                    fi = {'x': f.x, 'y': f.y, 'item': f.item, 'type': f.type}
                    fov.append(fi)
                eq = [copy.copy(e).__dict__ for e in pc.equipment]
                for e in eq:
                    e['owner'] = None
                di = {'fov': fov, 'x': pc.coords[0], 'y': pc.coords[1], 'eq': eq,
                      'facing': pc.facing, 'uid': pc.uid, 'name': pc.name, 'health': pc.cur_hp,
                      'xp': pc.experience}
                data[pc.name]['playa'] = di
                data[pc.name]['npcs'] = npcs
        self.data['rooms'][msg['room']]['game'] = board
        return data
