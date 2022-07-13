from typing import Union
from media import TVMedia, PaperMedia
from heroes import Superman, ChuckNorris, SuperHero
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    TVMedia.make_news(place, hero.name)
    PaperMedia.make_news(place, hero.name)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())
