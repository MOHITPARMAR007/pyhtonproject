from functools import reduce

lst = [3, 5, 6, 7, 22, 44, 66, 77, 99, 33, 11]
print(lst)
# filter is used for kuch bhi saf karna ho lst me se jese even or odd
evens = list(filter(lambda x: x % 2 == 0, lst))
print(evens)
# map puri list me kuch opration karna ho tho
dobles = list(map(lambda x: x * 2, lst))
print(dobles)
# reduce
average = list(reduce(lambda a, b: int(a + b) / int(len(lst)), lst))
print(average)
