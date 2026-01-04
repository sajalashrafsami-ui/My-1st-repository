word = "Sajal"
chances = 5
GuessAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end=" ")
        else:
            print("_", end=" ")


    MyGuess = input(f"Your chances {chances}, guess the letter: ").lower()
    GuessAdd.append(MyGuess)

    if MyGuess not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in GuessAdd:
            done = False

if done:
    print(f"Congrats! The word is {word}")
else:
    print("You lose the game")
