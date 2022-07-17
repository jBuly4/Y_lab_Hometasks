from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def fire_a_gun(self):
        pass


class LaserWeaponNatural(ABC):

    @abstractmethod
    def incinerate_with_lasers(self):
        pass


class KungFu(ABC):

    @abstractmethod
    def kick(self):
        print('Kick!')


class GunWeapon(Weapon):

    def fire_a_gun(self):
        print('PIU!!! PIU!!')


class LaserEyeWeapon(LaserWeaponNatural):

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class OrdinaryKicks(KungFu):

    def kick(self):
        print('Kick!')

    def roundhouse_kick(self):
        print('Bump!')
