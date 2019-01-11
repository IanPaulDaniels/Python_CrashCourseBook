import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee('Ian', 'Daniels', 39000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
    
    def test_five_custome_raise(self):
        self.employee.give_raise(7000)

unittest.main()
        