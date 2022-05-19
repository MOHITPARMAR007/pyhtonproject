"""Create a food log file for each client
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
Use function"""


def getdate():
    import datetime
    return datetime.datetime.now()


print("health management program")
print("press :\n1 for rohan\n2 for mohan \n3 for harsh")
num1 = int(input(" Enter your choice :\n"))
if num1 == 1:
    print("What You want retrive or Log details")
    print("enter 1 for retrive \n 0 for Log")
    num2 = int(input())
    if num2 == 1:
        print("Which info do you want to see about food press f or for exercise press e")
        choice = str(input())
        if choice == 'f' or 'F':
            f = open("rohanfood.txt")
            print(f.read(), end="")
        elif choice == 'e' or 'E':
            a = open("rohan_exer.txt")
            print(a.read(), end="")
        else:
            print("error")


    elif num2 == 0:
        print("In which FILE you want to add on info  food press f or for exercise press e")
        str2 = str(input())
        if str2 == 'f' or 'F':
            f = open("rohanfood.txt", "a")
            dt = getdate()
            print(dt)
            str1 = input("write what u want to add : \n")
            print(str1)
            f.write(str1)
            f.write("\n")
            f = open("rohanfood.txt")
            print(f.read())
            f.close()
        elif str2 == 'e' or 'E':
            f1 = open("rohanexe.txt", "a")
            dt1 = getdate()
            print(dt1)
            st3 = input("write what u want to add in exercise : \n")
            print(st3)
            f1.write(st3)
            f1.write("\n")
            f2 = open("rohanexe.txt")
            print(f2.read())
            f2.close()
        else:
            print("wrong input!!!!!!")



    else:
        print("wrong choice!!!!!")
