# Определение классов в модулях и их подключение

# import lesson4_script_garden
from lesson4_script_garden import PotatoGarden

my_garden = PotatoGarden(5)
my_garden.are_all_ripe()

for _ in range(3):
    my_garden.grow_all()

my_garden.are_all_ripe()