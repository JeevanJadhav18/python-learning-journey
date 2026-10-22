#SET :is collection of unordered items
#collection = {1, 2, 3, 4}
collection = {1, 2, 2, 2, 4, "hello", "world", "world"} #it count repeated value only ones
print(collection)
print(type(collection))
print(len(collection)) #the length is 5 not 8 because it does not count repeated
collection = {} #empty dictionary
print(type(collection))
collection = set() #empty set
print(type(collection))