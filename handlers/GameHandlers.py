from handlers.BaseHandler import BaseHandler
import random


class NotdHandler(BaseHandler):
    def get(self, room):
        data = {}
        room = str(room)
        try:
            data['board'] = self.data['rooms'][room]['game']
        except KeyError:
            data['board'] = None
        if data['board']:
            try:
                self.data['rooms'][room]['players']
            except KeyError:
                self.data['rooms'][room]['players'] = {}
                for player in data['board'].players:
                    self.data['rooms'][room]['players'][player] = None

            if self.player() and self.player()['room'] == room:
                data['player'] = self.player()
            else:
                data['player'] = None

            name = None
            if data['player'] and data['player']['room'] == room:
                name = data['player']['player']
                if name not in [p.name for p in data['board'].players]:
                    name = None
            if not name:
                names = ['Juan', 'Jose', 'Miguel', 'Carlos', 'Jesus', 'Taco']
                name = random.choice(names)
                while name in [p.name for p in data['board'].players]:
                    name = random.choice(names)
                d = {'room': room, 'player': name}
                print 'new player', d
                data['board'].add_player(name)
                self.set_player(d)

            for player in data['board'].players:
                if player.name == name:
                    data['player'] = player
                    break
            data['room'] = room
            data['fov'] = data['board'].fov(data['player'])
            for player in data['board'].players:
                print player.__dict__

            self.data['rooms'][room]['game'] = data['board']
            self.render("notd.html", **data)
            #self.render("notd2.html", **data)
            #self.render("data_check.html", data=data)
        else:
            self.redirect('/')
