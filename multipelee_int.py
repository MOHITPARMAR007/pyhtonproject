class low_student:
    def __init__(self, hindi, english):
        self.hindi = hindi
        self.english = english


class aver_student:
    def __init__(self, hindi, english, maths, ss):
        self.hindi = hindi
        self.english = english
        self.maths = maths
        self.ss = ss


class topper(low_student, aver_student):
    def __init__(self, hindi, english, maths, ss, sc):
        self.hindi = hindi
        self.english = english
        self.maths = maths
        self.ss = ss
        self.sc = sc


roshan = low_student(43, 45)
vaibhav = aver_student(44, 45, 49, 62)
print(vaibhav.english)
