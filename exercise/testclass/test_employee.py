import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee=Employee('san','zhang',10000)
        self.pre_salary=self.employee.salary

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,self.pre_salary+5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(7500)
        self.assertEqual(self.employee.salary,self.pre_salary+7500)


unittest.main()
