import unittest
from employee_class import Employee


class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.employee1 = Employee('qiu', 'bin', 10000)
		self.salarys = 7000

	def test_give_default_raise(self):
		self.employee1.give_raise()
		self.assertEqual(self.employee1.salary, 15000)

	def test_give_custom_raise(self):
		self.employee1.give_raise(self.salarys)
		self.assertEqual(self.employee1.salary, 17000)


unittest.main
