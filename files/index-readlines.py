# "With" and "as" are reserved words that means behavior similar like a function
with open('load.csv') as file:
    content = file.readlines()

# Content is already open so you can work with it
header = content[:1] #returns just the first row [[Last_name, "First name", "SSN","Test1", "Test2", "Test3", "Test4", "Final", "Grade"],[2],[3]]
rows = content[1:] #returns everything except the first row
print("----------------CONTENT----------------")
print(content)
print("----------------------------------")
print("--------------HEADER--------------")
print(header)
print("---------------ROWS----------------")
print("----------------------------------")
print(rows)