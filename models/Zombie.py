from models.CharBase import Base
import datetime

fivehunna = datetime.timedelta(milliseconds=750)


class Zombie(Base):
    def __init__(self, tile, uid, zid=0, facing=0):
        self.init(hp=15, worth=5, uid=uid, tile=tile, delay=fivehunna)
        self.name = "Zombie"

    def regen(self):
        self.heal(2)
