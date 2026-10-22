#if elif else
#eg code :TRAFFIC LIGHT CODE
light = input("Light:")
if(light == "red" or light == "RED"):
    print("STOP")
elif(light == "yellow" or light == "YELLOW"):
    print("LOOK")
elif(light == "green" or light == "GREEN"):
    print("GO")
else:
    print("light is broken")



#EGCODE :grades of student 
# let consider (90 to 100 == A)(80 to 89 == B)(70 to 79 == C) (less than 70 == D)
marks =int (input("Marks:"))
if(marks >= 90):
    print("Student Grade is A.")
elif(marks >= 80 and marks < 90):
    print("Student Grade is B.")
elif(marks >= 70 and marks < 80):
    print("Student Grade is C")
else:
    print("Student Grade is D")

#Practice Question print(A = 5 & G = M)(A=2 & G=F)code
A = int (input("A:"))
G = input("M/F:")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 or G == "M"):
    print("fee is 300")
else:
    print("no fee")

#Single line if-else (Ternary Operator)
#<var> = <val1> if <condition> else <val2>
#code:
food = input ("food: ")
eat = "Yes" if food == "cake" else "no"
print(eat)

#<stt1> if <condittion> else <stt2>
#egg code:
food = input("food:")
print("sweet") if food == "cake" or food == "jalebi" else print ("no sweet")

#clever if
#<var> = (false_val, true_val)(<condition>)
#code
age = int(input("age:"))
vote = ("yes", "no") [age < 18]
print(vote)

#code:
sol = float(input("salary: "))
tax = sol*(0.1,0.2) [sol > 50000]
print(tax)