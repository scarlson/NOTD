from models.CharBase import Base
import datetime

fivehunna = datetime.timedelta(milliseconds=250)


class Player(Base):
    def __init__(self, tile, uid, name, facing=0):
        self.init(tile, uid, hp=100, facing=facing, experience=0,
                  worth=20, delay=fivehunna)
        self.name = name
