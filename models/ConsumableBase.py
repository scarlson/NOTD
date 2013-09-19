

class Consumable(object):
    def __init__(self):
        self.max_stack = 1
        self.cur_stack = 1
        self.owner = None
        self.name = self.__class__.__name__

    @property
    def count(self):
        return self.cur_stack

    def use(self):
        if self.cur_stack > 0:
            self.cur_stack -= 1
            self.effect(self.owner)
        if self.cur_stack == 0:
            self.owner.equipment.remove(self)

    def effect(self, target):
        raise

    def replenish(self, count):
        if self.cur_stack < self.max_stack:
            self.cur_stack += count
            if self.cur_stack > self.max_stack:
                self.cur_Stack = self.max_stack
