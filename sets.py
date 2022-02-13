from tkinter import S


s1=set()
print(type(s1))
l=[1,2,3,4,5]
s_from_list=set(l)
print(s_from_list)
print(type(s_from_list))
s2=set()

#it can add unique elements
s2.add(1)
s2.add(1)
s2.add(2)
s2.add(3)
s2.remove(3)
print(s2)

# taking union of two sets

s3=s2.union({1,2,3})
print(s2,s3)

# intersection
s4=s2.intersection(s3)
print(s3,s4)

#min and max values
print(min(s2))
print(max(s3))

# disjoint it returns true or false
print(s3.isdisjoint(s4))