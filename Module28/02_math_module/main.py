import math

class MyMath:
    def circle_length(self, radius):
        return 2 * math.pi * radius

    def circle_area(self, radius):
        return math.pi * radius ** 2

    def cube_volume(self, side):
        return side ** 3
    
    def sphere_surface_area(self, radius):
        return 4 ** math.pi * radius ** 2


my_math = MyMath()

print(my_math.circle_length(5))
print(my_math.circle_area(6))
print(my_math.cube_volume(5))
print(my_math.sphere_surface_area(6))