calculation = True
while calculation:
  number1 = int(input("choose a number:\n"))
  number2 = int(input("choose another number:\n"))
  operation = input(
      "choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
  )
  if operation == "+":
    print("result:", number1 + number2)
  elif operation == "-":
    print("result:", number1 - number2)
  elif operation == "*":
    print("result:", number1 * number2)
  elif operation == "/":
    print("result:", number1 / number2)
  else:
    calculation = False
