class Employee:
    """The employee class to track salary."""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

    def print_employee(self):
        print(f"{self.first} {self.last} makes {self.salary} annually.")