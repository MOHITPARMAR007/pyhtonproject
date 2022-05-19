class std:
    no_of_leaves = 5

    def __init__(self, name, roll, std):
        self.name = name
        self.roll = roll
        self.std = std

    def getdata(self):
        print(f"name is {self} roll no is {self} ")
    @classmethod
    def change_leaves(cls,new_leaves):
       cls.no_of_leaves = new_leaves


    @staticmethod
    def printgood(string):
        print("hi ji"+string)


mohit = std("mohit", 32, 12)
print(mohit.std)
print(mohit.no_of_leaves)
mohit.change_leaves(23)
print(mohit.no_of_leaves)
#karan=std.re_str("karan 88 9")
mohit.printgood("mohit")
