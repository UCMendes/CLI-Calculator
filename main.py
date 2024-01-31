import re


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
    # Calc first expression in list
    total = expression(in_list[0], in_list[1], in_list[2])

    # Dealing with multiple signs in sequence ex: "2+2+2+2"
    count = 4
    while count <= (len(in_list) - 1):

      # Add previous answer to next elements:
      total = expression(str(total), in_list[count - 1], in_list[count])
      count += 2
    return total
  except ZeroDivisionError:
    return "Error: Cannot divide by 0"
  
# set regex rules for determining a valid expression
NUMBER = re.compile(r"[0-9]{1,}")
LOW_PRIO_SIGN = re.compile(r"[\+\-]")
HIGH_PRIO_SIGN = re.compile(r"[\*\/]")
# bracket = re.compile(r"\([.]{1,}\)")


EXP = re.compile(
  # Any amount of LOW_PRIO_SIGN followed by NUMBER
  # THEN EITHER one HIGH_PRIO_SIGN followed by any amount of LOW_PRIO_SIGN
  # OR At least one LOW_PRIO_SIGN
  # Followed by NUMBER, repeat line 47 any amount of times.
  rf"({LOW_PRIO_SIGN.pattern})*" +
  NUMBER.pattern +
  rf"""(({HIGH_PRIO_SIGN.pattern}({LOW_PRIO_SIGN.pattern})*|({LOW_PRIO_SIGN.pattern}){{1,}}){NUMBER.pattern})*""") 

# EXP but at least one sequence of line 53 needs to occur.
EXPLICIT_EXP = re.compile(
  rf"({LOW_PRIO_SIGN.pattern})*" +
  NUMBER.pattern +
  rf"""(({HIGH_PRIO_SIGN.pattern}({LOW_PRIO_SIGN.pattern})*|({LOW_PRIO_SIGN.pattern}){{1,}}){NUMBER.pattern}){{1,}}""")


while True:
  valid_calc = False
  while not valid_calc:
    calc_store = str(input("""Enter what you want to calculate, or enter 'X' to exit: """))
    if calc_store == "X":
      print("Thanks for using this calculator.")
      exit()
    calc_store = calc_store.replace(" ", "")

    # Send error message if no expressions are seen in input
    if re.fullmatch(EXP, calc_store) == None:
      print("Invalid expression.")
    else:
      valid_calc = True


  # Split calculation into components of number and sign
  calc_list = re.split(rf"({NUMBER.pattern})", calc_store)
  calc_list = [i for i in calc_list if i != ""]
  print(calc_list)

  # First pass through expression, to calc all times/divides
  for i, item in enumerate(calc_list):

    # If current item is an expression, find result
    if re.fullmatch(EXPLICIT_EXP, item):
      temp_list = re.split(rf"({HIGH_PRIO_SIGN.pattern})", item)
      calc_list[i] = perform_calculation(temp_list)

  # End current if there are no more expressions to calc
  if len(calc_list) == 2:
    print(f"Answer: {calc_list[0] + calc_list[1]}")
    continue
  elif len(calc_list) == 1:
    print(f"Answer: {calc_list[0]}")
    continue
  
  # Second pass for plus and minus, then output answer
  print(f"Answer: {perform_calculation(calc_list)}")

