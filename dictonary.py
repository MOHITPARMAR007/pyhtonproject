d1={ "mohit" : "chicken",
     "gautami": " sweets ",
     "mummy": "dal",
     "rohan":"pizza",}
     #"aditya" :("br":"rat ka khana" ,"lu":" meggie", "din" :"roti sabji")

print(d1)
print(d1.keys())
print(d1["mohit"])
d2=d1.copy()
del d2["mohit"]
print(d2)
print(d2.get("gautami"))
d2.update({"mohit":"veg"})
print(d2)
