lst1 = [27,97,3.14,True,'Hardik']
lst2 = ['Sharma',45,18,21.5,False]

# APPEND
lst1.append("Jammu")
lst2.append("Kashmir")    
print(" After appending lst 1 : " , lst1)
print(" After appending lst 2 : " , lst2)

#INSERT
lst1.insert(2,5)
lst2.insert(0,"Hardik")              
print(" After inserting : ", lst1)
print(" After inserting : ", lst2)

#EXTEND
lst1.extend(lst2)
print(" After extend : ", lst1)

#REMOVE
lst1.remove("Hardik")
lst2.remove(45)
print(" After removing : ", lst1)
print(" After removing : ", lst2)

#DELETE
del lst1[2]
del lst2[4]
print(" After deleting : ", lst1)
print(" After deleting : ", lst2)

#SORT (Descending)
lst3 = [22,34,87,87.87]
lst3.sort(reverse=True)
print(" After sorting : " , lst3)

OUTPUT ---

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 7 questions.py"
 After appending lst 1 :  [27, 97, 3.14, True, 'Hardik', 'Jammu']
 After appending lst 2 :  ['Sharma', 45, 18, 21.5, False, 'Kashmir']
 After inserting :  [27, 97, 5, 3.14, True, 'Hardik', 'Jammu']
 After inserting :  ['Hardik', 'Sharma', 45, 18, 21.5, False, 'Kashmir']
 After extend :  [27, 97, 5, 3.14, True, 'Hardik', 'Jammu', 'Hardik', 'Sharma', 45, 18, 21.5, False, 'Kashmir']
 After removing :  [27, 97, 5, 3.14, True, 'Jammu', 'Hardik', 'Sharma', 45, 18, 21.5, False, 'Kashmir']
 After removing :  ['Hardik', 'Sharma', 18, 21.5, False, 'Kashmir']
 After deleting :  [27, 97, 3.14, True, 'Jammu', 'Hardik', 'Sharma', 45, 18, 21.5, False, 'Kashmir']
 After deleting :  ['Hardik', 'Sharma', 18, 21.5, 'Kashmir']
 After sorting :  [87.87, 87, 34, 22]
