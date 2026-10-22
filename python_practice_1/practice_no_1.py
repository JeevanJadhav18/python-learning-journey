"""#Practice test
#Write a program to input 2 no. & print their sum.
num1 = int(input("FIRST VALUE: "))
num2 = int(input("SECOND VALUE: "))
sum = num1 + num2
print("Total value: ", sum)

#WAP to input side of a square squar & print its area.
side = float(input("Enter square side :"))
print("area=", side * side)

#WAP TO INPUT 2 FLOATING POINT NUMBERS & PRINT THEIR AVERAGE.
a = float(input("enter first :"))
b = float(input("enter second :"))

print ("avg:",(a+b)/2)"""

#WAP TO INPUT 2 int number, a and b. Print True if a IS GREATER THAN EQUAL TO B. IF NOT PRINT FALSE.
a = int(input("a :"))
b = int(input("b :"))
print("T/F: ", a >= b)
a = int(input("A:"))
b = int(input("B:"))
c = ("false", "true")[a >= b]
print(c)