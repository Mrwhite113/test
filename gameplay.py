import unit
import gamedb
import battle

# class Game:
#     _name = 'Hrenb'

if __name__ == '__main__':
    p1 = unit.Unit('Poul')
    p2 = unit.Unit('Ttis')
    fa = battle.Battle([p1, p2], gamedb.location)
    fa.attack(p1, p2)
    fa.attack(p2, p1)


    print(p1.unit_stats())
    print(p2.unit_stats())
