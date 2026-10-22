#tuple is immutablelike string
tup = (87,64,33,95,76)
print(type(tup))
print(tup[0])
print(tup[2])
#tup[0]= 5#tup is immutable it cannot change the value in the tupple

#for empty values
tup = ()
print(type(tup))
print(tup)

#for single values
tup = (1,) # if we want the tuple for ingle vlue than we should give coma after it
print(tup)
print(type(tup))

tup = (1) # if we want the tuple for ingle vlue than we should give coma after it
print(tup)# if we not give the coma then it will tell like int, or string
print(type(tup))

tup = ("string") # if we want the tuple for ingle vlue than we should give coma after it
print(tup)# if we not give the coma then it will tell like int, or string
print(type(tup))

#slicing in tupple
tup = (2,4,6,5,8)
print(tup[0:3])
print(tup[0:])

#methods/ func of tupples
tup = (1,2,3,4,2,2)
print(tup.index(2))#return idx of first ocuurence
print(tup.count(2))#return the count of element