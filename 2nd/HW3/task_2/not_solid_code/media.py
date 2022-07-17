from abc import ABC, abstractmethod


class Media(ABC):

    @classmethod
    @abstractmethod
    def make_news(cls, place, hero_name):
        pass


class TVMedia(Media):

    @classmethod
    def make_news(cls, place, hero_name):
        place_name = getattr(place, 'name', 'place')
        if isinstance(place_name, list):
            print(f'Urgent GALAXY TV News!\n{hero_name} saved the planet with coordinates {place_name}!')
        else:
            print(f'Urgent TV News!\n{hero_name} saved the {place_name}!')


class PaperMedia(Media):

    @classmethod
    def make_news(cls, place, hero_name):
        place_name = getattr(place, 'name', 'place')
        if isinstance(place_name, list):
            print(f'GALAXY notPAPER NEWS!\n{hero_name} saved the planet with coordinates {place_name} and killed the '
                  f'enemy!')
        else:
            print(f'PAPER NEWS!\n{hero_name} saved the {place_name} and killed the enemy!')
