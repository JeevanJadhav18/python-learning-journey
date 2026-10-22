#instead of writing the list one by one we can write in one line while using []
marks = [95, 70, 85, 60]
print(marks[2])#list is similar to string the concept like indexing is used  
print(type(marks))
print(len(marks))# to find the length                          
marks[0] = 80#in python we can do changes in list
print(marks)


#list slicing : is similar string 
#list_name[starting_idx ; ending_idx] ending_idx is not included
marks = [50,80,65,72,54]
print(marks[1:4])
print(marks[-3:-1])#the negative index is also used