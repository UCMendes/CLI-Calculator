import unittest
import re
import calc_regex as cr

# Assuming spaces have already been removed
class TestRegex(unittest.TestCase):

    def test_inputs_1(self):
        temp_list = re.split(cr.NUMBER, "2")
        temp_list = [i for i in temp_list if (i != "" and i is not None)]
        self.assertEqual(temp_list, ["2"])

    def test_inputs_2(self):
        temp_list = re.split(cr.NUMBER, "2+2**2")
        temp_list = [i for i in temp_list if (i != "" and i is not None)]
        self.assertEqual(temp_list, ["2", "+", "2", "**", "2"])

    def test_inputs_3(self):
        temp_list = re.split(cr.NUMBER, "2.2")
        temp_list = [i for i in temp_list if (i != "" and i is not None)]
        self.assertEqual(temp_list, ["2.2"])

if __name__ == '__main__':
    unittest.main()
