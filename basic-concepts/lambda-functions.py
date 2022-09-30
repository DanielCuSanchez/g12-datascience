# Lambda functions: Is a reserved word for using to create shorter versions of functions.

# lambda arguments : expression

sum = lambda n1, n2 : n1 + n2


def sum1(n1,n2):
  return n1 + n2

#print(sum(10,1112))
#print(sum1(10,1112))


# Lambda's power

def myMainFunction(factor):
  return lambda x: x * factor
  # x * 2


myDoubleFunction = myMainFunction(2)
myFourFunction = myMainFunction(4)


print(myDoubleFunction(487484))
print(myFourFunction(910))