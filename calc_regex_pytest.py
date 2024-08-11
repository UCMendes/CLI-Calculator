import unittest
import re
import calc_regex as cr

# Assuming spaces have already been removed
class TestRegex(unittest.TestCase):

    def test_inputs_1(self):
        temp_list = re.split(rf"({cr.NUMBER.pattern})", "2")
        temp_list = [i for i in temp_list if i != ""]
        self.assertEqual(temp_list, ["2"])

    def test_inputs_2(self):
        temp_list = re.split(rf"({cr.NUMBER.pattern})", "2+2")
        temp_list = [i for i in temp_list if i != ""]
        self.assertEqual(temp_list, ["2", "+", "2"])

if __name__ == '__main__':
    unittest.main()