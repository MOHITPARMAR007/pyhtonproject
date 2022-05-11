num1=18
i=0
print("you have to gusse my number ")
print("rules : .you have only 9 chances")
while(i<=9) :
    num2=int(input("enter the number"))
    if num2> num1 :
        print("try small value")
        i=i+1
        print("no of guss left is ",9-i)
    elif i == 10:
        print("you loose")
        continue
    elif num2<num1 :
        print("try greater value")
        i = i + 1
        print("no of guss left is ", 9 - i)
    elif i == 10:
        print("you loose")
        continue
    elif num2==num1 :
        print(" congo u won")
        break
    elif i==10 :
        print("you loose")
    else :
        print("error!!!!!!!")



