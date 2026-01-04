while True:
    (ans)= input("Do you want to play it?[Yes/No]:")
    if ans=="Yes":
        print("Welcome to the game")
        ans = input("Where do you want to go?[Jungle/Cave]:")
        if ans=="Jungle":
            print("You lost")
        elif ans=="Cave":
            print("You see a lion sleeping")
            ans= input("What will you do?[fight/run]:")
            if ans=="fight":
                print("You lost")

            else:
                print("Survived, Won the game")
                break
    else:
        print("End")
        break