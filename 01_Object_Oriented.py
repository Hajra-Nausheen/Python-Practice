#  We have two types of approach of programming
# 1. Object Oriented Programming
# 2. Functional approach
# object oriented programming mai classes and object ke sath deal krte 
# Class: Is a blue print to create objects. We can create multiple objects in a single class.


# Tum chirago ki tarah rah mai chlte rehna
# Har Andhere ko Ujalo mai bdalte rehna


class employee:   
    language ="Py"  # This is an class attibute
    salary =1500000
    role = "Data Analyst"


hajra = employee()   
hajra.name = "Hajra"  # This is an instance attibute
print(hajra.name,hajra.salary,hajra.language)

arshad = employee()
arshad.name = "Arshad"
print (arshad.name,arshad.salary,arshad.role )

#  Here name is instance attribute and salary and language are class attribute as they directly
# belong to the class
