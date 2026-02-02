class Student:
    def record(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
    def display(self):
        print(self.name)
        print(self.age)
        print(self.roll_no)
s1=Student()
s1.record("chanchal",19,8)
s1.display()



    