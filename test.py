import unittest
from my_module import sum2numbers, split_string_by_comma, write_to_file

class Test(unittest.TestCase):
    def test_function1(self):
        result = sum2numbers(5, 8)
        self.assertEqual(result, 13)


    def test_function2(self):
        result = split_string_by_comma("Helow,dog,bag")  # Замените на ваши реальные аргументы
        self.assertEqual(result, ["Helow", "dog", "bag"])

    def test_function3(self):
        result = write_to_file("file.txt","Helow Nazar")  # Замените на ваши реальные аргументы
        self.assertTrue(result)