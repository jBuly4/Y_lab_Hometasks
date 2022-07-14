from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder
from weapons import GunWeapon, LaserEyeWeapon, OrdinaryKick, RoundhouseKick


class SuperHero(ABC):
    def __init__(self, name: str, can_use_ultimate_attack: bool = False):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass


class Superman(SuperHero):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        OrdinaryKick.kick()

    def ultimate(self):
        LaserEyeWeapon.incinerate_with_lasers()


class ChuckNorris(GunWeapon, SuperHero):
    def __init__(self):
        super(ChuckNorris, self).__init__('Chuck Norris', True)

    def attack(self):
        print('Chuck Norris fist punch to enemy chin!')

    def ultimate(self):
        RoundhouseKick.roundhouse_kick()
