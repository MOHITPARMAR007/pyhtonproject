"""num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2st number:"))
try:
    def add(num1,num2) :
         addi=num1+num2
         return addi
         ans=add(num1,num2)
         print(ans)
except Exception as e:
    print(e)
print(" exception handeling is done")"""
print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)



print("This line is very important")