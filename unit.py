import random


class Unit:
    _defens = None
    _hp = None
    _name = None


    def __init__(self, u_name):
        self._name = u_name
        self._hp = 100
        self._att = random.randint(1,7)
        self._defens = random.randint(1,10)

    def unit_item(self, unit, item):
        info = f''' User {unit} have {item}'''
        return info

    def unit_stats(self):
        stat_notif = f'''
        User {self._name} have next stats:
        HP = {self._hp};
        ATTACK = {self._att};
        DEFENSE = {self._defens};'''
        return stat_notif

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, item):
        if item._addhp is not None:
            self._hp += item._addhp
            notif = f"{self._name} updated her(is) stats!"
        else:
            notif = f"{self._name} didn`t update her(is) stats"
        return notif

    @property
    def defens(self):
        return self._hp

    @defens.setter
    def defens(self, item):
        if item._adddef is not None:
            self._defens += item._adddef
            notif = f"{self._name} updated her(is) stats!"
        else:
            notif = f"{self._name} didn`t update her(is) stats"
        return notif
