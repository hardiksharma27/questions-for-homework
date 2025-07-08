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