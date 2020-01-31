import random
import gamedb

class Battle:
    _rounds = None
    _location = None
    _units = None

    def __init__(self, unit, loc, round = 20):
        loc_id = random.randint(0, 7)
        self._rounds = round
        self._location = loc[loc_id]
        self._units = len(unit)

    def double(self):
        db = random.uniform(0.0, 100.0)
        if db >= 80: return True
        else: return False

    def attack(self, unit, enemy):
        if self.double(): dobuledm = 2
        else: dobuledm = 1
        rpb = enemy._defens * random.uniform(0.0, 0.7)
        crit = random.uniform(1.0, 3.0)
        enemy._hp -= abs(unit._att - rpb) * crit * dobuledm
