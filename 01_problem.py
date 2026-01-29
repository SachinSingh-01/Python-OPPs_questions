# Write a simple class Student and create one object of it.
class Student:
    name="Sachin Singh"
s1=Student()
print(s1.name)

# another method
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("Sachin Singh")
print(s1.name)