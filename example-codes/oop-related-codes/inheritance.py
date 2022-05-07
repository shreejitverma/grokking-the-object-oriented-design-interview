class Person(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):

    def is_employee(self):
        return True


# Driver code
emp = Person("Person 1")
print(f"{emp.get_name()} is employee: {emp.is_employee()}")

emp = Employee("Employee 1")
print(f"{emp.get_name()} is employee: {emp.is_employee()}")