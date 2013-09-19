from models.WeaponBase import Base
import random


class Unarmed(Base):
    def __init__(self):
        self.init(owner=None,min_damage=5,max_damage=7,range=1)


class Bat(Base):
    def __init__(self):
        self.init(owner=None,min_damage=10,max_damage=20,range=1)


class Sword(Base):
    def __init__(self):
        self.init(owner=None,min_damage=25,max_damage=50,range=1)


class Pistol(Base):
    def __init__(self):
        self.init(
            owner=None,
            min_damage=25,
            max_damage=35,
            range=5,
            max_ammo = 30,
            mag_size = 6,
            current_mag = 6)
