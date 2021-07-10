import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.worker = Employee("Alice", "Smith", 45000)

    def test_default_raise(self):
        self.worker.give_raise()
        self.assertEqual(50000, self.worker.salary)

    def test_alternative_raise(self):
        self.worker.give_raise(25000)
        self.assertEqual(70000, self.worker.salary)


if __name__ == '__main__':
    unittest.main()