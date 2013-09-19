import random


class Base(object):
    def __init__(self, owner=None, min_damage=0, max_damage=0, max_ammo=0, mag_size=0, current_ammo=0, current_mag=0, range=0):
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.max_ammo = max_ammo
        self.mag_size = mag_size
        self.current_ammo = current_ammo
        self.current_mag = current_mag
        self.range = range
        self.owner = None
        self.name = self.__class__.__name__
        
    def __eq__(self,other):
        if type(self) == type(other):
            return self.__dict__ == other.__dict__
        return False

    @property
    def damage(self):
        return random.randint(self.min_damage,self.max_damage)

    def fire(self, target):
        if self.max_ammo > 0 and self.current_mag > 0:
            target.damage(self.damage)
            self.current_mag -= 1
        elif self.max_ammo == 0:
            target.damage(self.damage)

    def reload(self):
        if self.max_ammo > 0 and self.current_ammo > 0:
            self.current_ammo += self.current_mag
            if self.current_ammo > self.mag_size:
                self.current_mag = self.mag_size
                self.current_ammo -= self.mag_size
                return True
            else:
                self.current_mag = self.current_ammo
                self.current_ammo = 0
                return True
        return False

    init = __init__
