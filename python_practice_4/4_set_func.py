collection = set()

collection.add(1)#use to add the value
collection.add("hello")
collection.add(2)
collection.add(2)
print(len(collection))

#collection.remove(1) # use to remove the value
collection.clear()# it empty the whole set
#collection.remove(7)#error
print(len(collection))

names ={"hello","apna","colloge","coding"}

print(names.pop())# this is used to pop any random value from set
print(names.pop())
print(names.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))# combine to set va=lue and return new set
print(set1.intersection(set2))# give the intersection values