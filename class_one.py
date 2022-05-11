class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumferance(self):
        return 2 * 3.14 * self.radius


c1 = circle(5)
print(c1.circumferance())
print(c1.area())
c2 = circle(2)
print(c2.circumferance())
