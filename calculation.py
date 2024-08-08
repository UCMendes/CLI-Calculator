"""Import Regex module"""
import re
import calc_regex as cr


class Calculation:


    def __init__(self, calc_list):
        self.calc_list = calc_list

    def simple_calc(self, term1, sign, term2):
        """
        Simple arithmetic calculator, to assist with function of
        total_plus_minus().

        Parameters:
            (int) term1, first term of the calculation.
            (str) sign, sign to be used in calculation.
            (int) term2, second term of the calculation

        Returns:
            (int) total, result of the calculation.
        """
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
        return None
    
    def total_times_divide(self):
        """
        Performs all multiplication and division in calc_list.

        Parameters:
            No Parameters.

        Returns:
            (list) calc_list, result of list af.
        """
        try:
            # Calc first expression in list
            for i in range(len(self.calc_list) - 1):
                while i + 1 < len(self.calc_list) and \
                    re.search(cr.HIGH_PRIO_SIGN.pattern, self.calc_list[i + 1]):
                    self.calc_list[i] = str(self.simple_calc(
                        self.calc_list[i],
                        self.calc_list[i + 1],
                        self.calc_list[i + 2]
                    ))
                    del self.calc_list[i + 2], self.calc_list[i + 1]
        except ZeroDivisionError:
            return "Error: Cannot divide by 0"
        
    def check_times_divide(self):
        if ("*" in self.calc_list) or ("/" in self.calc_list):
            return True
        return False

    def total_plus_minus(self):
        """
        Totals elements in calc-list together, beginning from 
        the first element to the last.

        Parameters:
            No Parameters.

        Returns:
            (int) total, result of the calculation.
        """
        # Only less than 2 elements in calc_list = join (if necessary) and return
        if 1 <= len(self.calc_list) <= 2 :
            return "".join(self.calc_list)
        # Calc first expression in list
        total = self.simple_calc(self.calc_list[0], self.calc_list[1], self.calc_list[2])

        # Dealing with multiple signs in sequence ex: "2+2+2+2"
        count = 4
        while count <= (len(self.calc_list) - 1):

            # Add previous answer to next elements:
            total = self.simple_calc(str(total), self.calc_list[count - 1], self.calc_list[count])
            count += 2
        return total

    def filter_signs(self):
        """
        Determines if signs in the calculation are indicating positivity/negativity.
        If there are multiple in sequence, runs reduce_sign_sequence() to reduce to a single equivalent.
        if a "*/" is seen before "+-", reduces "+-" before joining result to the following letter.

        Parameters:
            No parameters.

        Returns:
            Nothing is returned.
        """
        first_section = True
        for count, section in enumerate(self.calc_list):
            signs_found = len(re.findall(cr.LOW_PRIO_SIGN.pattern, section))
            if signs_found >= 1 and first_section:
                first_section = False
                self.calc_list[count + 1] = \
                  self.reduce_sign_sequence(section) + self.calc_list[count + 1]
                self.calc_list[count] = ""

            elif signs_found >= 1 and \
              re.search(cr.HIGH_PRIO_SIGN.pattern, section):
                self.calc_list[count + 1] = \
                  self.reduce_sign_sequence(section[1:]) + self.calc_list[count + 1]
                self.calc_list[count] = self.calc_list[count][0]

            elif signs_found >= 2:
                self.calc_list[count] = self.reduce_sign_sequence(section)

            else:
                first_section = False
        self.calc_list = [i for i in self.calc_list if i != ""]

    def reduce_sign_sequence(self, sign_string):
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
        print(self.calc_list)
