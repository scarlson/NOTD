from models.Weapons import Unarmed
import datetime


class Base(object):
    def __init__(self, tile, uid, delay, hp=0, equipment=None, facing=0,
                 worth=0, experience=0):
        self.max_hp = hp
        self.cur_hp = self.max_hp
        self.equipment = equipment or []
        self.carry_size = 6
        self.tile = tile
        self.facing = facing
        self.worth = worth
        self.experience = experience
        preitem = self.tile.item
        self.tile.item = Unarmed()
        self.pickup()
        self.tile.item = preitem
        self.uid = uid
        self.delay = delay
        self.time = datetime.datetime.now()

    def __eq__(self, other):
        if type(self) == type(other):
            return self.uid == other.uid
        return False

    @property
    def can_move(self):
        return datetime.datetime.now() >= self.time + self.delay

    def turn_left(self):
        if self.facing == 0:
            self.facing = 5
        else:
            self.facing -= 1

    def turn_right(self):
        if self.facing == 5:
            self.facing = 0
        else:
            self.facing += 1

    def forward(self):
        if not self.can_move:
            return False
        if self.facing == 0:
            self.y -= 1
        if self.facing == 1:
            self.x += 1
        if self.facing == 2:
            self.x += 1
            self.y += 1
        if self.facing == 3:
            self.y += 1
        if self.facing == 4:
            self.x -= 1
        if self.facing == 5:
            self.x -= 1
            self.y -= 1
        self.time = datetime.datetime.now()
        return True

    def backward(self):
        if not self.can_move:
            return False
        if self.facing == 0:
            self.y += 1
        if self.facing == 1:
            self.x -= 1
        if self.facing == 2:
            self.x -= 1
            self.y -= 1
        if self.facing == 3:
            self.y -= 1
        if self.facing == 4:
            self.x += 1
        if self.facing == 5:
            self.x += 1
            self.y += 1
        self.time = datetime.datetime.now()
        return True

    def move(self, tile):
        if self.can_move:
            self.tile = tile
            self.time = datetime.datetime.now()
            return True
        return False

    def face(self, facing):
        self.facing = facing

    def refresh(self):
        raise
        #self.cur_energy = self.max_energy

    @property
    def coords(self):
        return (self.tile.x, self.tile.y)

    @property
    def dead(self):
        if self.cur_hp <= 0:
            return True
        return False

    def heal(self, dmg):
        if self.cur_hp < self.max_hp:
            self.cur_hp += dmg
            if self.cur_hp > self.max_hp:
                self.cur_hp = self.max_hp

    def damage(self, dmg):
        if self.cur_hp > 0:
            self.cur_hp -= dmg

    def distance(self, target):
        distance = 0
        ox, oy = self.coords
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

    def attack(self, weapon, target):
        if not self.can_move:
            return False
        if self.distance(target) > weapon.range:
            return False
        if weapon in self.equipment:
            weapon.fire(target)
            self.time = datetime.datetime.now()
            return True
        return False

    def pickup(self):
        if len(self.equipment) < self.carry_size and self.tile.item:
            self.tile.item.owner = self
            self.equipment.append(self.tile.removeItem())
            return True
        return False

    def drop(self, item):
        if item in self.equipment and not self.tile.item:
            item.owner = None
            self.tile.item = item
            self.equipment.remove(item)
            return True
        return False

    init = __init__
