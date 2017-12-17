import unittest
from name_function import get_formatted_name


class TestNameFuntion(unittest.TestCase):
	def test_first_name(self):
		formatted_name = get_formatted_name('qiu', 'bin')
		self.assertEqual(formatted_name, 'Qiu Bin')

	def test_middle_name(self):
		formatted_name = get_formatted_name('qiu', 'bin', 'xiao')
		self.assertEqual(formatted_name, 'Qiu Xiao Bin')


unittest.main
