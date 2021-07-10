from employee import Employee

alice = Employee("Alice", "Smith", 45000)
bob = Employee("Bob", "Wilson", 40000)

print("\nWe have two employees:")
alice.print_employee()
bob.print_employee()

print("\nIt's performance raise time")
alice.give_raise()
bob.give_raise(8000)

print("\nUpdated employee information")
alice.print_employee()
bob.print_employee()