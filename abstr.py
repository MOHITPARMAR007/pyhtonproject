from abc import ABCMeta,abstractmethod
class shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0


class rectangle(shape):
    type = "reactangel"
    side = 4

    def __init__(self, l, b):
        self.length = l
        self.breath = b

    def printarea(self):
        return self.length * self.breath


rec1 = rectangle(5, 4)
print(rec1.printarea())
