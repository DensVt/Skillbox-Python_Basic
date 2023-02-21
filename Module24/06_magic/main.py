from element import Water, Air, Fire, Earth

water = Water()
air = Air()
fire = Fire()
earth = Earth()

storm = water + air
dust = air + earth
Lightning = air + fire

print(water.title, "+", air.title, "=", storm.title)
print(air.title, "+", earth.title, "=", dust.title)
print(air.title, "+", fire.title, "=", Lightning.title)

