
import random
r=random.randint(1,20)
chances=5
while(True):
    print("\nGUESS A NUMBER")
    inp=int(input())
    if(inp>r):
        print("\nYOU HAVE GUESSED GREATER NUMBER, PLEASE GUESS SMALLER NUMBER")
        chances=chances-1
        print("\nChances left are",chances)
        if(chances==0):
            print("YOU ARE OUT OF CHANCES")
            break
    elif(inp<r):
        print("\nYOU HAVE GUESSED SMALLER NUMBER, PLEASE GUESS GREATER NUMBER")
        chances=chances-1
        print("\nChances left are",chances)
        if chances==0:
            print("YOU ARE OUT OF CHANCES")
            break
    else:
        print("\nYOU HAVE CORRECTLY GUESSED THE NUMBER\n")
        break;