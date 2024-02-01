"""Import Regex module"""
import re


class Calculation:


    def __init__(self, calc_list):
        self.__calc_list = calc_list

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

    def full_calc(self):
        try:
            if len(self.__calc_list) == 2:
                return "".join(self.__calc_list)
            # Calc first expression in list
            total = self.simple_calc(self.__calc_list[0], self.__calc_list[1], self.__calc_list[2])

            # Dealing with multiple signs in sequence ex: "2+2+2+2"
            count = 4
            while count <= (len(self.__calc_list) - 1):

                # Add previous answer to next elements:
                total = self.simple_calc(str(total), self.__calc_list[count - 1], self.__calc_list[count])
                count += 2
            return total
        except ZeroDivisionError:
            return "Error: Cannot divide by 0"

    def filter_signs(self):
        """
        Determines if signs in the calculation are indicating positivity/negativity.
        If there are multiple in sequence, runs resolve_signs() to reduce to a single equivalent.
        if a "*/" is seen before "+-", reduces "+-" before joining result to the following letter.


        Parameters:
            No parameters.

        Returns:
            Nothing is returned.
        """
        first_sect = True
        for count, sect in enumerate(self.__calc_list):
            if len(re.findall(LOW_PRIO_SIGN.pattern, sect)) >= 2:
                if first_sect:
                    first_sect = False
                    self.__calc_list[count + 1] = self.resolve_signs(sect) + self.__calc_list[count + 1]
                    self.__calc_list[count] = ""
                else:
                    self.__calc_list[count] = self.resolve_signs(sect)
        self.__calc_list = [i for i in self.__calc_list if i != ""]

    def resolve_signs(self, sign_string):
        """
        Reduces multiple "+-" signs in sequence to a single equivalent:
        Example:
            "++" returns "+"
            "--" returns "+"
            "+-+" returns "-"

        Parameters:
            (str) sign_string, the string to reduce

        Returns:
            (str) result, a string of either "+" or "-" 
        """
        result = "+"
        for symbol in sign_string:
            if symbol == "-" and result == "+":
                result = "-"
            elif symbol == "-" and result == "-":
                result = "+"
        return result

    def get_status(self):
        """
        Prints the current contents of calc_list.
        
        Parameters:
            No parameters.

        Returns:
            Nothing is returned.
        """
        print(self.__calc_list)



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
    temp_list = re.split(rf"({NUMBER.pattern})", calc_store)
    temp_list = [i for i in temp_list if i != ""]
    curr = Calculation(temp_list)
    curr.filter_signs()

    # Second pass for plus and minus, then output answer
    print(f"Answer: {curr.full_calc()}")
