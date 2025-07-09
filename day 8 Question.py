tup1 = (27,45.18,False,"hardik")
tup2 = 23,3.14,True,"sharma"
print(" Original tup1 " , tup1)
print(" Original tup2 " , tup2)

#updating the tuple 
tup1 = (65,76,True,"Manik")
tup2 = 32,87.2,False,"Aryan"
print(" Updated tup1 " , tup1)
print(" updated tup2 " , tup2)

#acessing any three elements
print(" First element of tup1 " , tup1[0])
print(" Second element of tup1 " , tup1[1])
print(" Third element of tup1 " , tup1[2])
print(" First element of tup2 " , tup2[0])
print(" Second element of tup2 " , tup2[1])
print(" Third element of tup2 " , tup2[2])

#counting the occurence 
tup3 = (12,23,12,"Kartike")
tup4 = 23,32,43,23,"Sarnal",23
print("Count of 12 " , tup3.count(12))
print("Count of 23 " , tup4.count(23))

#length of these tuples
print("Length of tup1 " , len(tup1))
print("Length of tup2 " , len(tup2))
print("Length of tup3 " , len(tup3))
print("Length of tup4 " , len(tup4))


OUTPUT -----

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 8 Question.py"
 Original tup1  (27, 45.18, False, 'hardik')
 Original tup2  (23, 3.14, True, 'sharma')
 Updated tup1  (65, 76, True, 'Manik')
 updated tup2  (32, 87.2, False, 'Aryan')
 First element of tup1  65
 Second element of tup1  76
 Third element of tup1  True
 First element of tup2  32
 Second element of tup2  87.2
 Third element of tup2  False
Count of 12  2
Count of 23  3
Length of tup1  4
Length of tup2  4
Length of tup3  4
Length of tup4  6
 Concatenated tuple(tup+tup2) (65, 76, True, 'Manik', 32, 87.2, False, 'Aryan')
Repeated tuple 19 times  (65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan', 65, 76, True, 'Manik', 32, 87.2, False, 'Aryan')
PS C:\next yug classes> 

#concatenation
joined_tup = tup1 + tup2
print(" Concatenated tuple(tup+tup2)", joined_tup)

#repeat 19 times
print("Repeated tuple 19 times " , joined_tup*19)
