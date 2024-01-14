import re
import math


def calc_result(term1, sign, term2):
  term1 = int(term1)
  term2 = int(term2)
  if sign == "+":
    return term1 + term2
  elif sign == "-":
    return term1 - term2
  elif sign == "*":
    return term1 * term2
  elif sign == "/":
    return term1 / term2


# set regex rules for determining a valid expression
number = re.compile(r"\-?[0-9]{1,}")
sign = re.compile(r"[\*\+\-\/]")
expression = re.compile(number.pattern + rf"({sign.pattern}{number.pattern})*")

# Get expression from user, make sure it's valid
end = False

while not end:
  valid_calc = False
  while not valid_calc:
    calc_store = str(input("Enter what you want to calculate, or enter 'X' to exit: "))
    if calc_store == "X":
      print("Thanks for using this calculator.")
      exit()
    calc_store = calc_store.replace(" ", "")
    if re.fullmatch(expression, calc_store) == None:
      print("""Invalid expression.
  There needs to exist at least one whole number, followed by a symbol, followed by another whole number.
  Example formats include "2 + 2" and "-4 / 2".
            """)
    else:
      valid_calc = True

  # Split calculation into components of number and sign
  calc_list = re.split(rf"({sign.pattern})", calc_store)
  # Calculate and output answer
  answer = calc_result(calc_list[0], calc_list[1], calc_list[2])
  print(f"Answer: {answer}")



