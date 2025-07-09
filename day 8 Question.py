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

#concatenation
joined_tup = tup1 + tup2
print(" Concatenated tuple(tup+tup2)", joined_tup)

#repeat 19 times
print("Repeated tuple 19 times " , joined_tup*19)