def add_nums(x,y):
    try:
        x = float(x)
        y = float(y)
    except ValueError as exp_type:
        print("you have to provide numbers to add: {}".format(exp_type))
    return float(x)+float(y)

def divide_nums(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    else:
        return x / y

class Employees:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        try:
            self.first = first.capitalize()
            self.last = last.capitalize()
        except Exception as expt:
            print("first and/or last name not valid: {}".format(expt))
        try:
            self.pay = float(pay)
        except ValueError as err:
            print("payment must be a number: {}".format(err))

        self.tot_promotions = 0
        self.record_promotions = {}

    @property
    def email(self):
        return "{}@ie-freiburg.mpg.de".format(self.last.lower())

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def raise_pay(self, ra=None):
        self.tot_promotions +=1

        if ra:
            self.record_promotions[self.tot_promotions] = ra
            self.pay = int(self.pay * ra)
        else:
            self.record_promotions[self.tot_promotions] = self.raise_amt
            self.pay = int(self.pay * self.raise_amt)

def main():
    employee = Employees("FRANCESCO","FERRARI",3000)
    # employee = Employees(20,"FERRARI","france")
    print(employee.first, employee.last, employee.email, employee.pay)
    print(employee.tot_promotions, employee.record_promotions)
    employee.raise_pay()
    print(employee.pay, employee.tot_promotions, employee.record_promotions)
    employee.raise_pay(1.1)
    print(employee.pay, employee.tot_promotions, employee.record_promotions)


if __name__ == "__main__":
    main()
