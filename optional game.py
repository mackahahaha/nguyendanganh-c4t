n= "programmer"
words= list(n)
import random
random.shuffle(words)
print(*words)
answer = str(input("Your answer:"))
if answer == n:
    print ("You win")
else:
    print("hahaha")
input("Enter to escape")