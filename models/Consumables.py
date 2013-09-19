from models.ConsumableBase import Consumable


class Beans(Consumable):
    def effect(self, target):
        if hasattr(target,'heal'):
            target.heal(30)
        else:
            self.replenish(1)


class Bandages(Consumable):
    def effect(self, target):
        if hasattr(target, 'heal'):
            target.heal(30)
        else:
            self.replenish(1)
