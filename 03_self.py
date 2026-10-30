class employee:
    language= "Python"
    salary = 1500000
    

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

hajra = employee()
# hajra.language= "SQL"
# hajra.getinfo()
employee.getinfo(hajra)
    