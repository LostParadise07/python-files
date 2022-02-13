# creating dictionary
from this import s
from turtle import update


d={'asrar':92,'jamee':90,'abhishek':90}

# printing dictionary
print(d)

# dictionaries are unordered mapping of elements

# adding element in dictionary
d['jameel']=1
d['haseeb']=30
d['qwerty']=22
print(d)

# accessing elements in dictionary
for i in d:
    print(i,d[i])

# changing value of key
d['haseeb']=32
print(d)

# getting key and values
print(d.keys())
print(d.values())

#deleting key 
del d['qwerty']
print(d)

# printing values of keys
print(d['asrar'])

# checking if key exists
if('asrar' in d):
    print("yes")
else:
    print("no")

#length of dictionary
print(len(d))

# we can not acess elements like
# print(d[2])
# as elements are unordered

# dictionary can have lists as values
n={1:[1,2,3],2:[2,3,4]}
print(n)
   

