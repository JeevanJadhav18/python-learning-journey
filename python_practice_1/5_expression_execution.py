#Expression Execution
# String & Numeric values can operate together with *
A,B = 2,3
Txt = "@"
print (2*Txt*3)

# String & String can operate together
A,B = "2",3
Txt = "@"
print ((A+Txt)*B)

#Numeric values can operate with all arithmentic
A,B = 2,3
C = 4
print(A+B*C) 

#Arithmetic expresssion with Integers and float will result in float
A,B = 10, 5.0
C = A*B
print(C)

#RESULT OF DIVISION OPERATER WITH TWO INTEGERS IS ALWAYS FLOAT
A,B = 1,2
C = A / B
print(C)

#Integer DIvision with float and int will give int displayed as float
A,B = 1.5,3
C = A // B
print(C, A/B)
#floor gives closes integer, which is lesser than or equal to the float value
#Result of (A//B) is same as floor(A/B)
# 1.2=1, 8.99=8, -5.2=-6, -7.6=M-8
A,B = 12,5
C = A//B
print(C)

#Remainder is negative when is denominater is negative

A,B = 5,-2#5,2#-5,2
C = A%B
print(C)

