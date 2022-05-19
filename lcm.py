def user_input():
    a = input("enter value")
    b = input("enter value")
    return (a, b)


def add(a, b):
    return a + b


a, b = user_input()
c = add(a, b)
print(c)
