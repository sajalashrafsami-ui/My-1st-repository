import random
while True:
    print(random.randint(1,6))
    playagain= input("Y/N= ")
    if playagain =="Y":
        continue
    else:
        print("Gameover")
        break