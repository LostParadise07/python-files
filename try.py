# code in python

#taking string 1 as input
print("Please enter the first String")
string1=input()

# taking string 2 as input
print("Please enter the second String but this string should be substring of first")
string2=input()

#string 1 to upper
print("The upper case of This is the first String is ",string1.upper())

#string 1 to lower
print("The lower case of This is the first String is ",string1.lower())

#string 2 to upper
print("The upper case of This is the second String is ",string2.upper())

#string 2 to lower
print("The lower case of This is the second String is ",string2.lower())

#printing first string with its length
print("The first string is",string1,"with a length",len(string1))

#printing second string with its length
print("The second string is",string2,"with a length",len(string2))

#printing first character of first and second string rsepectively
print("The first character in first string is",string1[0])
print("The first character in second string is",string2[0])


# printing first string from second word
str1=string1.split()[2::]
print("The first string from second word is",str1)


# # printing second string from second word
str2=string2.split()[2::]
print("The second string from second word is",str2)

# string 3 as input
string3=input()

#replacing string 2 with string 3 in string 1
str3=string1.replace(string2,string3)
print(str3)
