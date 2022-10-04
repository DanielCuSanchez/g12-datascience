from random import choice

def generatePassword(quantity):
  capital_letters = ('A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M', 'N','Ñ','O', 'P','Q','R','S','T','U','V','X','Y','Z')
  lower_case = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
  numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
  symbols = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"', " ")
  all_characters = capital_letters +  lower_case + numbers + symbols

  password = []

  for x in range(quantity):
    char = choice(all_characters)
    # print(x, " === ", char)
    password.append(char)

  # ["2", "F", "$"]

  # password.join("") -> Javascript

  result = "".join(password)

  return result
