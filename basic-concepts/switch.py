# Equivalent to switch in python

input_text = input("Write a letter: ")

match input_text:
  case ('a' | 'A'):
    print("This a vowel")
  case ('e' | 'E'):
    print("This a vowel")
  case ('i' | 'I'):
    print("This a vowel")
  case ('o' | 'O'):
    print("This a vowel")
  case ('u' | 'U'):
    print("This a vowel")
  case _:
    print("Sorry is consonant")