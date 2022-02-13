import random
r=random.randint(1,25)

while(True):
    print("GUESS A NUMBER")
    inp=int(input())
    if(inp>r):
        print("YOU HAVE GUESSED GREATER NUMBER, PLEASE GUESS SMALLER NUMBER")
    elif(inp<r):
        print("YOU HAVE GUESSED SMALLER NUMBER, PLEASE GUESS GREATER NUMBER")
    else:
        print("YOU HAVE CORRECTLY GUESSED THE NUMBER")
        break;