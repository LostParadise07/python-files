print("enter the choice i.e 1 to chk criertia or press rest to return")
choice=int(input())
while(choice==1):
    print("enter the age")
    age=int(input())
    if(age>100):
        print("This age is logically not possible")
    elif(age>18):
        print("you can drive")
    elif(age==18):
        print("we will think about you")
    elif(age<18 and age>7):
        print("you are a child")
    else:
        print("it is your milk time")
        
    print("enter the choice i.e 1 to chk criertia or press rest to return")
    choice=int(input())

