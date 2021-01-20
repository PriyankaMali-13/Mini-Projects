class Employee:

    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def student(self):
        print(self.name,self.age)

stud1 = Employee('priya',23)
stud2 = Employee('renu',15)

stud1.student()
stud2.student()





