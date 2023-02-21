import random

carma_lvl = 500


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    day_karma = random.randint(1, 7)

    if random.randint(1, 10) == 5:
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception

    return day_karma


def main():
    karma = 0

    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                karma += one_day()
            except Exception as ex:
                fl_logger.write(f'{ex}\n')
            if karma >= 500:
                break

    print('Вы достигли Нирваны! ')
    print('Омм ')
