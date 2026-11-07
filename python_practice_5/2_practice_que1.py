#WHILE LOOP PRACTICE QUESTIONS
# #Q. 1 .print number from 1 to 100
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1
# print("Loop End")

# #Q. 2.print number from 100 to 1
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1
# print("Loop End")

# #Q. 3.print the multiplication table of a number n
# n = int( input("Enter Number :"))
# i = 1
# while i <= 10:
#     print(n * i)                          
                                                                                                   
#Q.4. PRINT THE ELEMENT OF THE FOOLOWING LIAT UAING A LOOP
# num = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(num):
#     print(idx)
#     idx += 1

# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

# #Q.5.SEARCH FOR an number x in this tupple using loop
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36

# i = 0
# while i < len(num):
#     if(num [i] == x):
#         print("Found at idx", i)
#         break           #here we use while loop keyword break to stop the further process 
#     else :
#         print("finding..")
#     i += 1
# print("end of loop")

# # FOR LOOP
# #Q.1. Print the element of the following list using a loop:

# list = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in list:
#     print(el)
# print("END")

#Q.2. SEARCH A NUMBER x in this tuple using loop:

tup = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x =  49

# for el in tup:
#     if (el == 49):
#         print("FOUND 49")
#         break
#     print (el)
# print("END")
idx = 0
for el in tup:
    if (el == x):
        print("number found at idx", idx)
        break 
    idx += 1