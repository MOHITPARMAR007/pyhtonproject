class Student:
    def __init__(self, first_name, sec_name):
        self.first_name = first_name
        self.sec_name = sec_name

    # self.email= print(f"{self.first_name}.{self.sec_name}@goggle.com")

    def print_details(self):
        print(f"the student is {self.first_name}.{self.sec_name}")
    @property

    def email(self):
        if self.first_name == None or self.sec_name == None:
            return "email is not found "
        return f"{self.first_name}.{self.sec_name}@goggle.com"
    @email.setter
    def email(self,string):
        names =string.split("@")[0]
        self.first_name=names.split(".")[0]
        self.sec_name = names.split(".")[1]
    @email.deleter
    def email(self):
        self.first_name=None
        self.sec_name=None

rollno1 = Student("mohit", "parmar")
print(rollno1.print_details())
print(rollno1.email)
rollno1.first_name = "mohit ji"
print(rollno1.email)
rollno1.email="this .that @goggle.com"
print(rollno1.email)
del rollno1.email
print(rollno1.email)
