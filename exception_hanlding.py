print("Enter num 1")
num1=int(input())
print("Enter num 2")
num2=input()
# this wil catch the error and without showing error will complete program
try:
    print("the sum is",num1+int(num2))

except Exception as c:
    print(c)

print("this is important line")
