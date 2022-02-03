# Hopefully a programme which takes in student details and returns their grades
def grade(percentage_grade, g_boundary):
    return f"{s_name}'s mark is {percentage_grade}, this is a(n) {g_boundary}"


# Student name
def student(s_name):
    return f"Student name is {s_name}"


s_name = input("Student name? ")
print(student(s_name))


# Homework Score
def homeworkscore(h_score):
    return f"Homework score has been set as {int(h_score)}"


h_score = int(input("Homework score /25? "))
if 0 < h_score <= 25:
    print(homeworkscore(h_score))
else:
    print("Score is not valid")


# Assessment score
def assessmentscore(a_score):
    return f"Assessment score has been set as {int(a_score)}"


a_score = int(input("Assessment score /50? "))
if 0 < a_score <= 50:
    print(assessmentscore(a_score))
else:
    print("Score is not valid")


# Final Exam score
def finalscore(f_score):
    return f"Final Exam score has been set as {int(f_score)}"


f_score = int(input("Final Exam score /100? "))
if 0 < f_score <= 100:
    print(finalscore(f_score))
else:
    print("Score is not valid")

# Grade in percentage form
total_grade = h_score + a_score + f_score
calcgrade = total_grade / float(1.75)
percentage_grade = int(calcgrade)


# Grade Boundary
def gradeboundary(g_boundary):
    return f"\n Here are {s_name}'s overall grade details; " \
           f"\n {s_name}'s mark is {percentage_grade}%, {s_name}'s grade = {g_boundary} "


if percentage_grade >= 95:
    g_boundary = "A*"
elif percentage_grade >= 85:
    g_boundary = "A"
elif percentage_grade >= 65:
    g_boundary = "B"
elif percentage_grade >= 50:
    g_boundary = "C"
elif percentage_grade >= 45:
    g_boundary = "D"
else:
    g_boundary = "F"

print(gradeboundary(g_boundary))
