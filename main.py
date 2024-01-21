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
low_prio_sign = re.compile(r"[\+\-]")
high_prio_sign = re.compile(r"[\*\/]")
# number plus any number of (sign and number)
exp = re.compile(number.pattern+rf"(({low_prio_sign.pattern}|{high_prio_sign.pattern}){number.pattern})*")
# Single numbers not accepted, must be an a full x sign y
explicit_exp = re.compile(number.pattern+rf"(({low_prio_sign.pattern}|{high_prio_sign.pattern}){number.pattern}){{1,}}")


while True:
  valid_calc = False
  while not valid_calc:
    calc_store = str(input("""Enter what you want to calculate, or enter 'X' to exit: """))
    if calc_store == "X":
      print("Thanks for using this calculator.")
      exit()
    calc_store = calc_store.replace(" ", "")
    # Send error message if no expressions are seen in input
    if re.fullmatch(exp, calc_store) == None:
      print("""Invalid expression.
  There needs to exist at least one whole number, followed by a symbol, followed by another whole number.
  Example formats include "2 + 2" and "-4 / 2".
            """)
    else:
      valid_calc = True

  # Split calculation into components of number and sign
  calc_list = re.split(rf"({low_prio_sign.pattern})", calc_store)

  # First pass through expression, to calc all times/divides
  for i, item in enumerate(calc_list):
    # If current item is an expression, find result
    if re.fullmatch(explicit_exp, item):
      temp_list = re.split(rf"({high_prio_sign.pattern})", item)
      temp_total = calc_result(temp_list[0], temp_list[1], temp_list[2])
      # Dealing with multiple times/divides in sequence
      count = 4
      while count <= (len(temp_list) - 1):
        # Add previous answer to next elements:
        temp_total = calc_result(str(temp_total), temp_list[count - 1], temp_list[count])
        count += 2
      calc_list[i] = temp_total

  # End current if there are no more expressions to compute
  if len(calc_list) < 3 or calc_list[0] == "":
    print(f"Answer: {calc_list[0]}")
    continue

  # Second pass through expression, to calc all add/minus
  answer = calc_result(calc_list[0], calc_list[1], calc_list[2])
  # Dealing with multiple add/minus in sequence
  count = 4
  while count <= (len(calc_list) - 1):
    # Add previous answer to next elements:
    answer = calc_result(str(answer), calc_list[count - 1], calc_list[count])
    count += 2
  
  # output answer
  print(f"Answer: {answer}")




