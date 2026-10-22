#you aregiven a list of subjects for student. assume one classroom is required for 1 subject. How many classrooms are neede by all students
subject = {"python", "java", "C+","python", "javascript", "java", "python", "java", "C+", "C"}
print(subject)
print("The no. of classroom need for student is :",len(subject))

#store following word meaning in a python dictionary
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts &figures"]
}
print(dict)

#WAP to enter marks of 3 subjects from the user &store them in a dictionary. Start with an empty dictionary& add one by onne. Use a subject name as key &marks as value.
"""marks ={}

x = int(input("enter phy:"))
marks.update({"phy" : x})

x = int(input("enter maths:"))
marks.update({"maths" : x})

x = int(input("enter chem:"))
marks.update({"chem" : x})

print(marks)"""


#figure out a way to store 9 &9.0 as seprate values in the set. (You can take help of build in data types)
#using string
#value = {9, "9.0"}
#print(value)# output 9, "9.0"
#using int, float
value = {
    "float" : "9.0",
    "int" : 9
}
print( value)