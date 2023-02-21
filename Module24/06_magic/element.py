class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None
class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None

class Shtorm:
    title = 'Шторм'
class Steam:
    title = 'Пар'
class Dirt:
    title = 'Грязь'
class Lightning:
    title = 'Молния'
class Dust:
    title = 'Пыль'
class Lava:
    title = 'Лава'