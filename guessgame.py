import random
import math

lower = int(input('Enter lower bound:-'))
upper = int(input('Enter upper bount:-'))
x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)),"chances to guess the integer!\n")
chances = math.log(upper - lower + 1, 2)
count  = 0
while count < chances:
    count += 1
    guess = int(input("Guess a number:-"))
    if x == guess:
        print("Congratulation you did it in ", count, "try")
        break
    elif x > guess:
        print("You guess too small")
    elif x < guess:
        print("You guess too high!")
    
    if count >= chances:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

