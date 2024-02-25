"""Imports"""
import re
import calc_regex as cr
import calculation as clc

def main():
    while True:
        valid_calc = False
        while not valid_calc:
            calc_store = str(input("""Enter what you want to calculate, or enter 'X' to exit: """))
            if calc_store == "X":
                print("Thanks for using this calculator.")
                exit()
            calc_store = calc_store.replace(" ", "")

            # Send error message if no expressions are seen in input
            if re.fullmatch(cr.EXP, calc_store) is None:
                print("Invalid expression.")
            else:
                valid_calc = True


        # Split calculation into components of number and sign
        temp_list = re.split(rf"({cr.NUMBER.pattern})", calc_store)
        temp_list = [i for i in temp_list if i != ""]
        curr = clc.Calculation(temp_list)
        curr.filter_signs()
        curr.get_status()

        # Second pass for plus and minus, then output answer
        print(f"Answer: {curr.full_calc()}")


if __name__ == "__main__":
    main()
