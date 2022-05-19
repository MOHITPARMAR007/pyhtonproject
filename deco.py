# decaraots allow us to do some changes in function without touching in the functions

def dec1(fun1):
    def nowexce():
        print("**__good evening__**")
        fun1()
        print("bye!!!")

    return nowexce()


@dec1
def dec2():
    print("god plz sab sahi kr do ")
    return 0


# dec2 = dec1(dec2) decorates ko likhne ka 2 tarika
print(dec2)
