"""
"r"=reading file----dafault
"w"=write in file
"x"=creating fle if it does not exist
"a"=append i.e adding more content to file
"t"=text mode
"+"=both read and write
"b"=binary mode
"""

p=open("asrar.txt")
content=p.read()
# printing content
print(content)
# closing file
p.close()

# printing file line by line
p=open("asrar.txt")

for line in p:
    print(line,end="")

print("/n")
p.close()

#printing few characters in file
p=open("asrar.txt")
content=p.read(7)
print(content)

p.close()
# reading lines using inbuilt function
p=open("asrar.txt")
print(p.readlines())
p.close()
#writing in file
p=open("asrar.txt","a")
content=p.write("\n i read in national institute of srinagar")
print(content)

p.close()
