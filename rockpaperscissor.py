import random
while True:
    print("welcome to rock,paper scissor game")
    a=["r","p","s"]
    comp=random.choice(a)
    p1=input("rock(r) paper(p) or scissor(s) quit(q)?")
    if(p1=="q"):
        break
    else:
        if(p1==comp):
            print("draw")
        elif((p1=="r" and comp=="s")or(p1=="p" and comp=="r")or(p1=="s" and comp=="p")):
            print("you won")
        else:
            print("you lost")
            
