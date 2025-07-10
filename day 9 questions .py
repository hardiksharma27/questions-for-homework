student_marks = {}  

student_marks['Alice'] = 85
student_marks['Bob'] = 92       
student_marks['Charlie'] = 78

student_name = input("Enter the student's name: ")   

if student_name in student_marks:
    print( "Marks :" , student_marks[student_name])
else:
    print("Student not found.")
