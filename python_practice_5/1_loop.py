#LOOP : IT is used to repeat the instruction
#it has 2 types : while loop & for loop

#WHILE LOOP
# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1
# #print(count)
# # here the count is called as iterator and
# # print("Hello") is called iteration

# i = 1
# while i <= 10 :
#     print("Jeevan", i)
#     i += 1

# #print the no. from 1 to 10
# i = 1
# while i <= 10 :
#     print(i)
#     i += 1
# print("loop end")

# #reverse loop 
# i = 10
# while i >= 1 :
#     print(i)
#     i -= 1
# print("end loop")

# # break & continue

# #break : used to terminate the loop when encountered.
# i = 1
# while i <=5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("loop end")

# # v SEARCH FOR an number x in this tupple using loop
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

# # continue : trminate execution in the current iteration & continue execution of the loop with the next iteration.

# i = 1
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue # by using this keyword we can skip the execution
#     print(i)
#     i += 1

#for loop 
#code
num = [ 1, 4, 6, 8, 14, 35]

for val in num:
    print(val)


tup = (1, 4, 6, 8, 14, 35)
for val in tup:
    print(val)

name = "Jeevan Jadhav"
for char in name:
    print(char)

# else : using to end the loop # IT IS OPTIONAL
num = [ 1, 4, 6, 8, 14, 35]

for val in num:
    print(val)
else:
    print("END")