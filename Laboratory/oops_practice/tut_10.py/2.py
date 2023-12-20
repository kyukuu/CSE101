class salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def gettotal(self):
        return self.pay*12

    def annual_salary(self):
        return self.pay*2+self.bonus


class employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_annual_salary = salary(pay, bonus)

    def total_salary(self):
        return self.obj_annual_salary.annual_salary()


emp = employee("kyuku", 25, 15000, 10000)
print(emp.total_salary())
