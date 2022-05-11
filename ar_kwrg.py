import kwargs as kwargs


def person(name, *data):  # 1 * is for kwargs that is used for multiple arguments
    print(name)
    print(data)


person("mohit", 19, 6264266726)


# 2** is used to pass key words in arguments
def person2(name, **other):
    print(name)


for i, j in other.items():
    print(i, j)

person2("parmar", age=19, mob_no=6264266726)
