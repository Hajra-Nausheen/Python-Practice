class employee:
    language= "Python"
    salary = 1500000
    role= "AI engineer"

    def __init__(self,name,salary,language,role):  # dunder method which is automatically called
         self.name=name
         self.salary=salary
         self.language = language
         self.role = role
         print("I am creating an object")
    

    def getinfo(self): 
       print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet ():
        print("Good Morning")

hajra = employee("Hajra",200000,"SQL","Data Scientist")
# hajra.name ="Hajra"
print(hajra.name, hajra.salary, hajra.language,hajra.role)

arshad = employee("Arshad",50000000,"R","AI engineer")
print(arshad.name,arshad.salary,arshad.language,arshad.role)



