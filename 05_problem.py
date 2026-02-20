# Create a class School that has a class variable school_name same for all students.
class School():
    school_name="Rose Bud Academy"
    def __init__(self,student_name):
        self.student_name=student_name
student1=School("Akash")
student2=School("Bikash")
print(f"Student 1: {student1.student_name}, School: {student1.school_name}")
print(f"Student 2: {student2.student_name}, School: {student2.school_name}")