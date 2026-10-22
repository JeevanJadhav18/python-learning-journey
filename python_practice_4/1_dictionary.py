#Dictionary
info = {
    "name" : "Jeevan",
    "subjects" : ["Python", "Java", "C"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "marks" : 94.5
}

print(type(info))
print(info["name"]) 
print(type("name"))
print(info["subjects"])
print(type("subjects"))
print(info["age"])  
print(type("topics"))
info["name"] = "adesh"#to change the value of the key #overwrite
info["surname"] = "Jadhav" #when we need to add the new key-value
print(info)
#print(info("surname")) if the key is not present it can show eror

null_dict = {}
null_dict[" name"] = "JEE"
print(null_dict)

#nested dictionary:it is a dictionary in the dictionary
student = {
    "name" : "Jeevan",
    "subject" : {
        "phy" : 95,
        "chem" : 99,
        "math" : 96,
    }
   
}
print(student)
print(student["subject"])
print(student["subject"]["phy"])