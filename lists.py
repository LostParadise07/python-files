from operator import length_hint


l=[9,12,3,3,7]

#printing the index value
print(l[4])

#list slicing
x=l[1:5]
print(x)

#adding or insertion at end
l.append(10)
print(l)

#adding another list b
b=[109,99]
l.extend(b)
print(l)

#inserting an element where 2 is index and 120 is value
l.insert(2,120)
print(l)

# sorting the list
l.sort()
print(l)

#deletion of an element where 3 is index
l.pop(6)
print(l)

#counting th element occurence
a=l.count(3)
print(a)

#length of list
a=len(l)
print(a)

# sum of elements
a=sum(l)
print(a)

#multilping the list that is size of list becomes 3 times list in this case
x=b*3
print(x)

#printing elements in list
for i in range(len(l)):
    print(l[i],end=', ')

# taking input from user
z=[]
for i in range(3):
    a=int(input())
    z.append(a)
print(z)