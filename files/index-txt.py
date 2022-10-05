# This is script is for opening a simple file

# This is how can we open a file, without any package
thisIsMyFile = open("./file.txt", "r")
print(thisIsMyFile.read())
# the logic here is to use the method from python for files
thisIsMyFile.close()