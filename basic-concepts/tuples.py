# Tuples are unchangeable and ordered, it accepts duplicated values

myTuple = ("Zaira","Ali", "David", "Joel", "Luis", "Luis")
# myTuple[5] = "Pedro" ⚠️


print(type(myTuple))
print(myTuple)


# Using constructor creation
myTupleExample = tuple((1,2,3,4,5))
print(type(myTupleExample))
print(myTupleExample)