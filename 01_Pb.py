# Create a class "Employee" for storing information of few programmers working at Microsoft
   
class employee:
    company ="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name 
        self.salary= salary
        self.pincode = pincode
        


hajra = employee("Hajra",5000000,431601)
print(hajra.name,hajra.salary,hajra.pincode,hajra.company)        


a = employee("Arshad",5000000,431601)
print(a.name,a.salary,a.pincode,a.company)  

s= employee("Shahed",5000000,431601)
print(s.name,s.salary,s.pincode,s.company) 

p = employee("P",5000000,431601)
print(p.name,p.salary,p.pincode,p.company)   

s = employee("S",5000000,431601)
print(s.name,s.salary,s.pincode,s.company)


s= employee("N",4000000,431602)
print(s.name,s.salary,s.pincode,s.company)
