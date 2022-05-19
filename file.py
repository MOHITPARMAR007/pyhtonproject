f = open("mohit.txt")   #yaha dusara argument jo hota hai waha pr  ode likha jata hain kis mode me apan file
print(f.readline(),end="")                            # ko use karna chate hain jese read mode  or text deafault hota hain
print(f.readline())

#content = f.read()
#read me agrumnts de sakte h int value jitne denge utne print kr dega words
#for line in f:
   # print(line,end="")


#print(content)

"""content = f.read(3)
print(content)
content = f.read(3)
print(content)"""


f.close()