import random
randomnum= random.randrange(1,100)
while True:
    userinput= int(input("Guess num:"))
    if userinput>randomnum:
        print("Too high")
        print(randomnum)
    elif userinput<randomnum:
        print("Too low")
        print(randomnum)
    else:
        print("Congrats!You matched the num")
        break