import random
secret= random.randint(1,10)
print("number guessing game")
print("guess a number between 1 and 10")
guess=int(input("enter your guess:"))
if guess== secret:
        print("you win!")
else:
     print("you lose!")
     print("correct number was:",secret)
