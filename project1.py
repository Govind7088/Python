# Number Guesses Game/Project.

print("#####******Welcome in Number Guesses Game.*******######\n")
name=input("Enter your good name: ")
print("Let's play the game, " + name)

import random
randomNumber = random.randint(1,100)

userGuess = None
guesses = 0
while (userGuess != randomNumber):
  userGuess = int(input("Enter Your guess Number: "))
  guesses+=1
  if(userGuess==randomNumber):
    print("You guessed it right!")
  else:
    if(userGuess>randomNumber):
      print("You guesses it wromg! Please enter a smaller number")
    else:
      print("You guesses it wrong! Please enter a larger number")

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
  highscore = int(f.read())\

if(guesses<highscore):
  with open("hiscore.txt", "w") as f:
    f.write(str(f"Your High Score is = {guesses}"))