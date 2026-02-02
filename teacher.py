class Teacher:
    def __init__(self,name,salary,sub):
        self.name=name
        self.salary=salary
        self.sub=sub
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.sub)
    def greet(self):
        print("ok thanking to you mam.....\n",self.name)
t1=Teacher("j",98000,"PAI")
t1.display()
t1.greet()


