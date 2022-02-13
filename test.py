from dataclasses import replace
from pickletools import string1


string1="this is my first"
string2="this"
string3="we"
str=string1.replace(string2,string3)
print(str)