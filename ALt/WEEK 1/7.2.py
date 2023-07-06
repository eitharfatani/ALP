number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = input()
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer: line 4

# What does '!=' mean?
  # Answer: not equal to

# How many variables are there in the code?
  # Answer: 2 

# How can you tell which lines of code are inside the loop?
  # Answer: all the lines under While are inside loop

# How many times will the loop repeat?
  # Answer: untill the user guesses the right number

# What has to happen to make the program run the last line of code?
  # Answer: guessing the right number

#task 3

mynumber = 9
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != mynumber:
  guess = input("Wrong! Guess again!")
print("You guessed it!")