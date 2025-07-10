student_marks = {}  

student_marks['Alice'] = 85
student_marks['Bob'] = 92       
student_marks['Charlie'] = 78

student_name = input("Enter the student's name: ")   

if student_name in student_marks:
    print( "Marks :" , student_marks[student_name])
else:
    print("Student not found")

OUTPUT --- 

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 9 questions .py"
Enter the student's name: Alice
Marks : 85
PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 9 questions .py"
Enter the student's name: Charlie  
Marks : 78
PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 9 questions .py"
Enter the student's name: Bob
Marks : 92
