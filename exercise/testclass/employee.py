class Employee():
    def __init__(self,firstname,lastname,salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary

    def give_raise(self,salary_raise=5000):
        self.salary+=salary_raise

    def show_info(self):
        print(self.firstname+' '+self.lastname+' salary='+self.salary)

