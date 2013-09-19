import heapq
import random
import copy
import time
import datetime
from models.Zombie import Zombie
from models.Player import Player
from models.Weapons import *
from models.Consumables import *

fivehunnams = datetime.timedelta(milliseconds=500)


class Field:
    def __init__(self, x, y, passable=True, type="Grass"):
        self.x = x
        self.y = y
        self.item = None
        self.char = None
        self.passable = passable
        self.type = type
        self.parent = None

    def __hash__(self):
        return hash(self.coords)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.coords == other.coords
        return False

    def rockify(self):
        self.type = "Rock"
        self.passable = False

    def treeify(self):
        self.type = "Tree"

    def getItem(self):
        return self.item

    def getChar(self):
        return self.char

    def removeItem(self):
        _item = self.item
        self.item = None
        return _item

    def removeChar(self):
        _char = self.char
        self.char = None
        return _char

    @property
    def coords(self):
        return self.x, self.y

    def neighbors(self, fields):
        possibles = [(self.x, self.y+1), (self.x, self.y-1),
                     (self.x-1, self.y), (self.x+1, self.y),
                     (self.x-1, self.y-1), (self.x+1, self.y+1)]
        return [field for field in fields if field.coords in possibles]


class Board:
    def __init__(self, height=10, width=12):
        self.height = height
        self.width = width
        self.pixel_w = self.width * 55 + 26
        self.pixel_h = self.height * 48 + 25
        b = []
        doh = 0
        for h in range(self.height):
            row = []
            for w in range(self.width):
                field = Field(w + doh, h)
                row.append(field)
            if h % 2 == 0:
                doh += 1
            b.append(row)
        self.rows = b
        self.turn = 0
        self.uid = 0
        from maps import maps
        for i, row in enumerate(self.rows):
            for j, field in enumerate(row):
                if maps['a'][i][j] == "Stone":
                    field.rockify()
                elif maps['a'][i][j] == "Entrance":
                    field.rockify()
                elif maps['a'][i][j] == "Tree":
                    field.treeify()

        if 0:
            for f in self.rows[0]:
                f.rockify()
            for f in self.rows[-1]:
                f.rockify()
            for row in self.rows:
                row[0].rockify()
                row[-1].rockify()
            while len(self.rocks) < len(self.fields) / 4:
                random.choice(self.valid_fields).rockify()
            while len(self.trees) < len(self.fields) / 10:
                random.choice(self.valid_fields).treeify()

    @property
    def items(self):
        return [f.item for f in self.fields if f.item]

    @property
    def astar_fields(self):
        return [f for f in self.fields if f.type == "Grass" and
                (f.char is None or f.char.name != "Zombie")]

    @property
    def valid_fields(self):
        return [f for fields in self.rows for f in fields if
                f.passable and not f.char]

    @property
    def fields(self):
        return [f for fields in self.rows for f in fields]

    @property
    def trees(self):
        return [f.char for f in self.fields if f.type == "Tree"]

    @property
    def rocks(self):
        return [f.char for f in self.fields if f.type == "Rock"]

    @property
    def chars(self):
        return [f.char for f in self.fields if f.char]

    @property
    def players(self):
        return [f.char for f in self.fields
                if f.char.__class__.__name__ == "Player"]

    @property
    def npcs(self):
        return [f.char for f in self.fields
                if f.char.__class__.__name__ == "Zombie"]

    def subtract(self, a):
        return a[0]-a[1]

    def distance(self, origin, target):
        distance = 0
        ox, oy = origin.coords
        tx, ty = target.coords

        while ox < tx and oy < ty:
            ox += 1
            oy += 1
            distance += 1
        while ox > tx and oy > ty:
            ox -= 1
            oy -= 1
            distance += 1
        while ox < tx:
            ox += 1
            distance += 1
        while ox > tx:
            ox -= 1
            distance += 1
        while oy < ty:
            oy += 1
            distance += 1
        while oy > ty:
            oy -= 1
            distance += 1

        return distance

    def aStar(self, origin, target):
        if hasattr(origin, 'name'):
            current = origin.tile
        else:
            current = origin
        current.parent = None
        if hasattr(target, 'name'):
            target = target.tile
        openSet = set()
        openHeap = []
        closedSet = set()

        def retracePath(self, c):
            path = [c]
            while c.parent is not None:
                c = c.parent
                path.append(c)
            path.reverse()
            for field in self.fields:
                if field.parent:
                    field.parent = None
            return path[1:]

        openSet.add(current)
        openHeap.append((0, current))
        while openSet:
            current = heapq.heappop(openHeap)[1]
            if current.coords == target.coords:
                return retracePath(self, current)
            openSet.remove(current)
            closedSet.add(current)
            for tile in current.neighbors(self.astar_fields):
                if tile not in closedSet:
                    tile.H = self.distance(tile, target)
                    if tile not in openSet:
                        openSet.add(tile)
                        heapq.heappush(openHeap, (tile.H, tile))
                    tile.parent = current
            if len(closedSet) > 10:
                return None
        return []

    def behind(self, coords, facing):
        x, y = coords
        if facing == 0:
            y += 1
        elif facing == 1:
            x -= 1
        elif facing == 2:
            x -= 1
            y -= 1
        elif facing == 3:
            y -= 1
        elif facing == 4:
            x += 1
        elif facing == 5:
            x += 1
            y += 1
        return x, y

    def front(self, coords, facing):
        x, y = coords
        if facing == 0:
            y -= 1
        elif facing == 1:
            x += 1
        elif facing == 2:
            x += 1
            y += 1
        elif facing == 3:
            y += 1
        elif facing == 4:
            x -= 1
        elif facing == 5:
            x -= 1
            y -= 1
        return x, y

    def fov(self, char):
        if char:
            front = self.getField(self.front(char.coords, char.facing))
            if front:
                twof = self.getField(self.front(front.coords, char.facing))
            center = self.getField(char.coords)
            fields = []
            fields.append(center)
            for field in center.neighbors(self.fields):
                fields.append(field)
            if front:
                for f in front.neighbors(self.fields):
                    for field in f.neighbors(self.fields):
                        if field not in fields:
                            fields.append(field)
            if front and twof:
                for f in twof.neighbors(self.fields):
                    for field in f.neighbors(self.fields):
                        if field not in fields:
                            fields.append(field)
            fs = list(fields)
            for f in fs:
                for field in f.neighbors(self.fields):
                    if field not in fields:
                        fields.append(field)
            return fields

    def spawn_items(self):
        w = [Bat(), Sword(), Beans()]
        while len(self.items) < len(self.valid_fields) / 50:
            f = random.choice(self.valid_fields)
            if not f.getItem():
                f.item = copy.copy(random.choice(w))

    def add_player(self, name):
        roar = random.choice(self.valid_fields)
        f = random.randint(0, 5)
        p = Player(roar, self.uid, name=name, facing=f)
        roar.char = p
        self.uid += 1

    def remove_player(self, player):
        player.tile.removeChar()

    def add_zombie(self):
        roar = random.choice(self.astar_fields)
        f = random.randint(0, 6)
        z = Zombie(roar, uid=self.uid, facing=f)
        roar.char = z
        self.uid += 1

    def removeChar(self, char):
        if hasattr(char, 'tile'):
            char.tile.removeChar()

    def getChar(self, coords):
        if self.getField(coords):
            return self.getField(coords).getChar()

    def getField(self, coords):
        for field in self.fields:
            if field.coords == coords:
                return field
        return None

    def turn_check(self):
        #if max([p.cur_energy for p in self.players]):
        #    return False
        start = time.time()
        self.zombies_turn()
        print "%.3f" % (time.time()-start)
        #[player.refresh() for player in self.players]
        #[zombie.refresh() for zombie in self.npcs]
        #self.turn += 1
        self.spawn_items()
        return True

    def zombies_turn(self):
        while len(self.npcs) < min([25, len(self.players)*4]):
            self.add_zombie()
        print len(self.npcs), 'zombies'
        for z in self.npcs:
            closest = None
            distance = 0
            if self.players:
                distance, closest = min([(self.distance(z, p), p) for p in self.players])
            if not closest or distance > 5 or closest.tile not in self.astar_fields:
                ts = [f.char for f in z.tile.neighbors(self.fields) if f.char and
                      f.char in self.players]
                while z.can_move:
                    if ts:
                        t = min([(p.cur_hp, p) for p in ts])[1]
                        self.face(z, t)
                        self.attack(z, t)
                    v = random.choice([f for f in z.tile.neighbors(self.astar_fields)])
                    self.face(z, v)
                    coords = z.coords
                    if z.move(v):
                        v.char = self.getField(coords).removeChar()
            if z.can_move:
                path = self.aStar(z, closest)
                while z.can_move:
                    if path and len(path) <= 1:
                        self.face(z, path[0])
                        if self.getChar(self.front(z.coords, z.facing)):
                            self.attack(z, self.getChar(self.front(z.coords, z.facing)))
                    elif path and len(path) > 1:
                        self.face(z, path[0])
                        coords = z.coords
                        if z.move(self.getField(self.front(coords, z.facing))):
                            self.getField(self.front(coords, z.facing)).char = \
                                self.getField(coords).removeChar()
                            path = path[1:]
                    else:
                        break

    def face(self, source, target):
        sx, sy = source.coords
        tx, ty = target.coords
        if sx == tx and sy > ty:
            source.facing = 0
        elif sx < tx and sy == ty:
            source.facing = 1
        elif sx < tx and sy < ty:
            source.facing = 2
        elif sx == tx and sy < ty:
            source.facing = 3
        elif sx > tx and sy == ty:
            source.facing = 4
        elif sx > tx and sy > ty:
            source.facing = 5

    def attack(self, source, target, item=None):
        if item:
            res = source.attack(item, target)
        else:
            res = source.attack(source.equipment[0], target)
        if res and target.dead:
            source.experience += target.worth
            if target in self.chars:
                self.removeChar(target)
        return [res, source, target]

    def action(self, player, key, item=None, target=None):
        if item and 'eq' in item:
            try:
                item = int(item[-1])
            except:
                item = None
        for p in self.players:
            if p.name == player:
                if item is not None:
                    try:
                        item = p.equipment[item]
                    except:
                        item = None
                if key == "w":
                    if self.getField(self.front(p.coords, p.facing)) and \
                            self.getField(self.front(p.coords, p.facing)) in self.valid_fields:
                        coords = p.coords
                        if p.move(self.getField(self.front(coords, p.facing))):
                            self.getField(self.front(coords, p.facing)).char = \
                                self.getField(coords).removeChar()
                elif key == "a":
                    p.turn_left()
                elif key == "d":
                    p.turn_right()
                elif key == "s":
                    if self.getField(self.behind(p.coords, p.facing)) and \
                            self.getField(self.behind(p.coords, p.facing)) in self.valid_fields:
                        coords = p.coords
                        if p.move(self.getField(self.behind(coords, p.facing))):
                            self.getField(self.behind(coords, p.facing)).char = \
                                self.getField(coords).removeChar()
                elif key == "z":
                    p.pickup()
                elif key == "x":
                    if item:
                        p.drop(item)
                        item.owner = None
                        self.getField(p.coords).item = item
                elif key == "e":
                    if item and hasattr(item, 'use'):
                        item.use()
                elif key == "space":
                    if item and hasattr(item, 'fire'):
                        if target:
                            self.attack(p, target, item)
                        elif self.getChar(self.front(p.coords, p.facing)):
                            self.attack(p, self.getChar(self.front(p.coords, p.facing)), item)
                self.turn_check()
                return True
        if self.players:
            self.turn_check()
        return False
