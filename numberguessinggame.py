import random
chance=5
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Welcome to number guessing game")
b=random.choice(a)
print("A number from 0-20 has been selected")
while chance!=0:
    c=int(input("Guess my number: "))
    if(b==c):
        print("Winner")
        break
    else:
        print("Try again")
    chance=chance-1
print("Game over, the answer is: ",b)
