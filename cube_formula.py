class cube:
    def __init__(self,side):
        self.side=side

    def volume(self):
        return self.side*self.side*self.side

    def curved_surface_area(self):
        return 5*self.side*self.side




side1=cube(4)
print(side1.volume())
print(side1.curved_surface_area())
