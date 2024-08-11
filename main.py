"""Imports"""
import re
from calc_regex import EXP, NUMBER
import calculation as clc


def main():
    while True:
        valid_calc = False
        while not valid_calc:
            calc_store = str(input("""Enter what you want to calculate, or enter 'x' to exit: """))
            if calc_store.lower() == "x":
                print("Thanks for using this calculator.")
                exit()
            calc_store = calc_store.replace(" ", "")

            # Send error message if no expressions are seen in input
            if re.fullmatch(EXP, calc_store) is None:
                print("Invalid expression.")
            else:
                valid_calc = True


        # Split calculation into individual components (number/sign)
        temp_list = re.split(NUMBER, calc_store)
        # Remove spaces
        temp_list = [i for i in temp_list if (i != "" and i is not None)]
        # Create object to store current state of expression
        print(temp_list)
        curr = clc.Calculation(temp_list)
        curr.filter_signs()
        curr.get_status()

        # Return answer
        if curr.check_times_divide():
            curr.total_times_divide()
        print(f"Answer: {curr.total_plus_minus()}")


if __name__ == "__main__":
    main()
