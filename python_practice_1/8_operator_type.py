# Types of operator
# arithmetic operator
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)# ans is always in float 
print(a%b) #remainder
print(a**b)#a^b

# relational? comparison operator  
a = 50
b = 20
print(a == b)#false # == equal symbol
print(a != b)# true # != not equal
print(a >= b)#true # >= greater than equal too
print(a > b) # true # > greater than
print(a <= b)# false # <=dsmaller than equal to
print(a < b)#falsee < smaller than

# assignmnet operator
num = 10
num += 10 #num + 10 #10+10 = 20
print("num : ",num)

num = 10
num -= 10
print("num : ",num)

num = 10
num *= 5
print("num : ",num)

num = 10
num /= 5
print("num : ",num)

num = 10
num %= 5
print("num : ",num)

num = 10
num **= 5
print("num : ",num)

# logical operator
a = 50
b = 30
#not operator
print(not False)
print(not True)
print(a>b)
print(not (a>b))
print(not (a<b))
#and operaror
val1 = True
val2 = False
print("AND OPERATOR:", (a == b) and (a > b))
print("OR operator:", (a == b) or (a > b))