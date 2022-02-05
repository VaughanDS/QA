# In a new Python file, create a class of students.
# It should contain the following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints the students average test score.

class Student:

    def __init__(self, name, age, class_):
        self.name = name
        self.age = int(age)
        self.class_ = class_

    def student_grade(self, s_grade1, s_grade2, s_grade3):
        average = (s_grade1 + s_grade2 + s_grade3) / 3
        return f"\n {self.name} achieved {average}"


New_student = Student("A", 12, "History")

print(New_student.student_grade(1, 2, 3))
