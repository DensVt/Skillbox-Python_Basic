class Circle:
    pi = 3.14159
    k = 2

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return self.r * self.r * self.pi
        # return 3.14 * self.r ** 2

    def perimeter(self):
        return 2 * self.r * self.pi

    def scale(self, k):
        self.r *= k
        return self.r

    def intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


circle = Circle()
print(circle.scale(5))
