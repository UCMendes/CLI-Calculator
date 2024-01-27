import re
import math


def expression(term1, sign, term2):
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
  
def perform_calculation(in_list):
  try:
    # Second pass through expression, to calc all add/minus
    total = expression(in_list[0], in_list[1], in_list[2])

    # Dealing with multiple signs in sequence
    count = 4
    while count <= (len(in_list) - 1):

      # Add previous answer to next elements:
      total = expression(str(total), in_list[count - 1], in_list[count])
      count += 2
    return total
  except ZeroDivisionError:
    return "Error: Cannot divide by 0"
  

# set regex rules for determining a valid expression
number = re.compile(r"\-?[0-9]{1,}")
low_prio_sign = re.compile(r"(?<![\*\/])[\+\-]")
high_prio_sign = re.compile(r"[\*\/]")
bracket = re.compile(r"\([.]{1,}\)")
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

  error_found = False
  # Split calculation into components of number and sign
  calc_list = re.split(rf"({low_prio_sign.pattern})", calc_store)
  print(calc_list)

  # First pass through expression, to calc all times/divides
  for i, item in enumerate(calc_list):

    # If current item is an expression, find result
    if re.fullmatch(explicit_exp, item):
      temp_list = re.split(rf"({high_prio_sign.pattern})", item)
      calc_list[i] = perform_calculation(temp_list)

  if error_found == True:
    continue

  # End current if there are no more expressions to calc
  if len(calc_list) < 3 or calc_list[0] == "":
    print(f"Answer: {calc_list[0]}")
    continue
  
  # Second pass for plus and minus, then output answer
  print(f"Answer: {perform_calculation(calc_list)}")

