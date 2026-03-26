
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_pay(self):
            return f"{self.base_salary}"

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, bonus):
        super().__init__(name, employee_id, base_salary, bonus)
        self.bonus = bonus

    def calculate_pay(self):
            return self.base_salary + self.bonus

class Intern(Employee):
    def __init__(self, name, employee_id, base_salary, hourly_rate, hours_worked):
        super().__init__(name, employee_id, base_salary, hourly_rate, hours_worked)

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

