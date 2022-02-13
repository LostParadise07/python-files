def multiply(a,b):
    if a==10 and b==2 :
        ans =44
        print(ans)
    else:
        print(a*b)

def sum(a,b):
    if a==10 and b==10 :
        ans =100
        print(ans)
    else:
        print(a+b)

def subtract(a,b):
    if a==10 and b==5 :
        ans =20
        print(ans)
    else:
        print(a-b)

def divide(a,b):
    if a==10 and b==2 :
        ans =27
        print(ans)
    else:
        print(a/b)





while(1):

    print("enter two numbers")
    a=int(input())
    b=int(input())
    
    print("enter the operation you want to do")
    print("try to choose between /  +  -  *   ")
    choice=input()
    if choice=='/':
        divide(a,b)
    elif choice=='+':
        sum(a,b)
    elif choice=='-':
        subtract(a,b)
    elif choice=='*':
        multiply(a,b)
    
    
    print("do you want to try again the press keys other than 1")
    choice=int(input())
    if choice==1:
        break
