import random
Words= ["gamers", "guild", "wonders", "marvelous", "excellent", "rainbow","apocalypse","artificial"]
play=input("Do you want to play? (yes or no)")
while play=="yes":
    word = random.choice(Words)
    jumble = list(word)
    random.shuffle(jumble)
    print(*jumble)
    answer = str(input("Your answer:"))
    if answer == word:
        print ("You win")
    else:
        print("Hahaha")
    play = input("Do you wanna play again? (yes or no)")
print("Thank you for playing")
input("Enter to exit")