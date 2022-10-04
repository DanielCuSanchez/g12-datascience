from passmodule import generatePassword


def run():
  quantity_chars = int(input("How long do you want your password: "))
  password = generatePassword(quantity_chars)
  print("Your new password is: ", password)


if __name__ == "__main__":
  run()





