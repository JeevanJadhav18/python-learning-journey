student = {
    "name" : "Jeevan",
    "subject" : {
        "phy" : 95,
        "chem" : 99,
        "math" : 96,
    }
   
}
print(student.keys())#returns keys
print(list(student.keys()))
print(student.values())#return all keys
print(list(student.values()))
print(student.items())#returns all the key-value
print(list(student.items()))
pairs = list(student.items())#
print(pairs[1])#it help in slicing
print(student.get("name")) #Returns the value according to key
print(student["name"]) #it gioves the same as .get
#but  if we take any non existing key it will show error
#print(student["name2"]) 
print(student.get("name2"))#but if we use this method it will show non so that the error will not show

#student.update({"city" : "Pune"}) #when we need to update something
new_dict = {"name" : "Sandesh", "age" : 18}
student.update(new_dict)
print(student)