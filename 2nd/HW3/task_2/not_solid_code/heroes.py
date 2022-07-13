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


# Проблема: Герой не должен заниматься оповещениями о своей победе, это задача масс-медиа.
# Несоблюден: Принцип единой ответственности.
# По SOLID: Вынести оповещение в отдельный класс, занимающийся выводом информации.
# Когда возникнут трудности? Добавьте оповещение о победе героя через газеты или через TV (на выбор)
# а также попробуйте оповестить планеты (у которых вместа атрибута name:str используется coordinates:List[float]).


# Проблема: Для каждого супергероя реализованы все методы обращения с оружием.
# Несоблюден: Принцип разделения интерфейса
# По SOLID: Создать классы-миксины для каждого оружия
# Когда возникнут трудности? Попробуйте запретить Чаку норрису пользоваться лазерами из глаз!

# Проблема: У разных супергероев разные суперспособности
# Несоблюден: Принцип открытости/закрытости
# По SOLID: Каждого супергероя реализовать как наследника SuperHero и вместо изменения базового класса
# переопределять нужные методы
# Когда возникнут трудности? Когда в вашем коде поселится вся команда Мстителей

# Проблема: Сигнатура метода изменилась. Если мэр города обратится к супермену как к супергерою у Кларка
# возникнут проблемы с атакой
# Несоблюден: Принцип подстановки Барбары Лисков
# По SOLID: Не допускать таких вольностей
# Когда возникнут трудности? При первой же битве