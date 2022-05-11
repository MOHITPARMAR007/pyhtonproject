class school:
    no_of_leaves=20
    def __init__(self,aname,aroll,astd):
        self.name=aname
        self.roll=aroll
        self.std =astd

    def getdata(self):
        print(f"name: {self.name} std :{self.std} roll no :{self.roll}")
    @classmethod


mohit=school("mohit",32,12)

print(mohit.getdata())
"""
mohit = school()
gautami = school()
mohit.name="mohit"
mohit.std=12
mohit.rollno=32
gautami.name="mohit"
gautami.std=12
gautami.rollno=16

print(mohit.getdata())
print(gautami.getdata())"""
