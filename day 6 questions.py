import sys #used this because while running the progam if age is smaller then 21 we have top exit but without,
           #import sys () we cannot exit the program.
name = input("Enter the name: ")
age = int(input("Enter the age: "))

if age < 21:
    print("NO INVESTMENT")   
    sys.exit()
    
elif 21 <= age < 30:
    print("Growth Stage")
elif 30 <= age < 40:
    print("Stabilizing Stage")
elif 40 <= age < 50:
    print("Peak Earning")
elif 50 <= age < 60:
    print("Transition to retirement")
else:
    print("Capital Preservation")

income = int(input("Enter the income: "))
if income < 300000 :
    print("Invest in: PPF or FD")
elif income < 700000:
    print("Invest in: HDFC Balanced Advantage Fund")
else:
    print("Invest in: Equity Mutual Funds + Retirement Plans")


OUTPUT ---

 A ...if we enter age smaller then 21 then
PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 6 questions.py"
Enter the name: hardik 
Enter the age: 18
NO INVESTMENT

B..... 
PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 6 questions.py"
Enter the name: hardik
Enter the age: 55
Transition to retirement
Enter the income: 1200000
Invest in: Equity Mutual Funds + Retirement Plans

