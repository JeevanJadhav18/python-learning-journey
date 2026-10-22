#slicing is for accessing the part of string
#and it is mainly use in ML
str = "Jeevan Jadhav"
print(str[1:4])#where the ending idx is not inclded
print(str[:7])#it starts from 0
print(str[7:len(str)])#in lat to take all the string we can use 'len(str)'
print(str[0:])#we can use nothing at end point

#negative index
#where the indexing start from -1from end point to 
#this is also use only in slicing
str = "apple"
print(str[-5:-4])
print(str[-4:-1])
