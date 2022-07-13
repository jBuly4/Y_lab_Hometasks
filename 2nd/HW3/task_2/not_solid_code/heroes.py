from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder
from weapons import GunWeapon, KungFuWeapon


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
        KungFuWeapon.superman_kick()

    def ultimate(self):
        print('Wzzzuuuup!')


class ChuckNorris(SuperHero):
    def __init__(self):
        super(ChuckNorris, self).__init__('Chuck Norris', True)

    def attack(self):
        GunWeapon.fire_a_gun()

    def ultimate(self):
        KungFuWeapon.roundhouse_kick()