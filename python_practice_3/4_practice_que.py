#practicce question

#wap to ask the user to enter names of their favuorite movies &storethem in a lsit
# movies = []
# movies.append(input("Enter 1st movie:"))
# movies.append(input("Enter 2nd movie:"))
# movies.append(input("Enter 3rd movie:"))

# print(movies)

#WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
list1 = [1,2,2,1,2]#[1,2,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1  == list1):
    print("PALINDROME")
else:
    print("NOT PALINDROME")

#WAP to count the no. of student with the "A" grade in the following tuple.
grades = ["C", "D", "A", "A", "B", "B","A"]
print(grades.count("A"))

#show the value in a list &sort them from "A" to "D"
grades = ["C", "D", "A", "A", "B", "B","A"]
grades.sort()
print(grades)