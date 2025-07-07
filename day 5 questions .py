str1 = "I am learning Python"
str2 = "Python is easy to learn as compared to Java"
joined_str = str1 + " " + str2
print(joined_str)
substring_1 = joined_str[:20]
print(substring_1)
substring_2 = joined_str[21:]
print(substring_2)
stepstr = joined_str[::9]
print(stepstr)
print(str2[-1]) # shows negative indexing 
print(str1.upper()) # converts string in upper case
print(str2.upper()) # converts string in upper case
print(str1.replace("Python","Java")) # replaces word 
print(str2.replace("Java","Python"))