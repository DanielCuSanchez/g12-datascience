# Lists comprehensions: They are a shorter version of a list declaration, it is used to filter, modify and remove data.

myList = ["Zaira","Ali", "David", "Joel", "Luis", "Luis"]

newList = [ element for element in myList if  element != "Luis" ]
newList2 = [ element.upper() for element in newList]
newList3 = [x for x in range(10)]

print(newList)
print(newList2)
print(newList3)