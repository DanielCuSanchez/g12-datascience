# Dictionaries: They are similar like objects in JS, the way the data is stored is with keys and values.

myCar = {
  "Brand": "Tesla",
  "Year": "2022",
  "Model": "S"
}

print(type(myCar))
print(myCar)


print("This loop just print the both keys and values")
for key,value in myCar.items():
  print(key+ " -> " + value)


print("This loop just print the keys")
for key in myCar.keys():
  print(key)


print("This loop just print the values")
for value in myCar.values():
  print(value)