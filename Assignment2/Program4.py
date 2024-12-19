students_score = int(input("Enter student's score : "))
if students_score >= 90 and students_score <= 100:
    print("Student's score is : A ")
elif students_score >= 80 and students_score <= 89:
    print("Student's score is : B")
elif students_score >= 70 and students_score <= 79:
    print("Student's score is : C")
elif students_score >= 60 and students_score <= 69:
    print("Student's score is : D")
else: 
    print("Student's score is : F")