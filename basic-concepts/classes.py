# Classes in python (POO)
class Student:
  name = ""
  age = ""

  def __init__(self, name, age):
    self.name = name
    self.age = age




newStudent = Student("Luis", 25)
newStudent1 = Student("David", 22)


print(newStudent.name)
print(newStudent1.name)