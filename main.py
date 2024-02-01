"""Import Regex module"""
import re


class Calculation:


    def __init__(self, init_list):
        self.__init_list = init_list

    def simple_calc(self, term1, sign, term2):
        term1 = int(term1)
        term2 = int(term2)
        if sign == "+":
            return term1 + term2
        if sign == "-":
            return term1 - term2
        if sign == "*":
            return term1 * term2
        if sign == "/":
            return term1 / term2

    def full_calc(self, input_list):
        try:
            # Calc first expression in list
            total = self.simple_calc(input_list[0], input_list[1], input_list[2])

            # Dealing with multiple signs in sequence ex: "2+2+2+2"
            count = 4
            while count <= (len(input_list) - 1):

                # Add previous answer to next elements:
                total = self.simple_calc(str(total), input_list[count - 1], input_list[count])
                count += 2
            return total
        except ZeroDivisionError:
            return "Error: Cannot divide by 0"

    # Get current calculation
    def get_status(self):
        """
        Prints the current contents of init_list.
        
        Parameters:
            No arguments.

        Returns:
            Nothing is returned.
        """
        print(self.__init_list)


# set regex rules for determining a valid expression
NUMBER = re.compile(r"[0-9]{1,}")
LOW_PRIO_SIGN = re.compile(r"[\+\-]")
HIGH_PRIO_SIGN = re.compile(r"[\*\/]")
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
        if re.fullmatch(EXP, calc_store) is None:
            print("Invalid expression.")
        else:
            valid_calc = True


    # Split calculation into components of number and sign
    calc_list = re.split(rf"({NUMBER.pattern})", calc_store)
    calc_list = [i for i in calc_list if i != ""]
    curr = Calculation(calc_list)

    # Second pass for plus and minus, then output answer
    print(f"Answer: {curr.full_calc}")
