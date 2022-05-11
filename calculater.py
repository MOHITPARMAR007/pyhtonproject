user_choise = int(input("enter 1 for uninary opreration \n  2 for arithmatic opration \n  3 for roots "))
if user_choise == 1:
    num = int(input("enter the number"))
    choice2 = int(input("1 for number of square \n2 for cube"))
    if choice2 == 1:
        x = num * num
        print(f"the square root of{choice2}is {x}")
    elif choice2 == 2:
        y = num * num * num
        print(f"the cube of {choice2}is {y}")

    else:
        print("wrong input!!!")


elif user_choise == 2:
    num = int(input("enter the number"))
    num2 = int(input("enter the 2 number"))

    choice2 = int(input("1 for add \n2 for sub \n3 for mul\n4division"))
    if choice2 == 1:
        ans = num + num2
        print(f"addition of 2 number is:{ans}")
    elif choice2 == 2:
        ans = num - num2
        print(f"subtraction of 2 number is:{ans}")

    elif choice2 == 3:
        ans = num * num2
        print(f"multiplication of 2 number is:{ans}")

    elif choice2 == 4:
        ans = num / num2
        print(f"division of 2 number is:{ans}")

    else:
        print("please try again")


elif user_choise == 3:
    type_one = int(input("if you want opration in interger press 1 or in floating 2"))

    if type_one == 1:

        root_num = int(input("enter the number"))
        root_choise = int(input("1 for square root 2 for cubr root"))
        if root_choise == 1:
            square = int(root_num ** 0.5)
            print(f"square of {root_num}is {square}")
        elif root_choise == 2:
            cube = int(root_num ** 0.3)
            print(f"square of {root_num}is {cube}")
        else:
            print("wrong input!!")



    elif type_one == 2:
        root_num = float(input("enter the number"))
        root_choise = float(input("1 for square root 2 for cubr root"))
        if root_choise == 1:

            square = float(root_num ** 0.5)
            print(f"square of {root_num}is {square}")
        elif root_choise == 2:
            cube = float(root_num ** 0.3)
            print(f"square of {root_num}is {cube}")
        else:
            print("wrong input!!")


else:
    print("wrong input")
