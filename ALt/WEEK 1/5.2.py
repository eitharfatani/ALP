'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: print Too Low!

# What happens if you input the guess '6'?
  # Answer: print Too High!

# What happens if you input the guess '5'?
  # Answer: print Correct!

# What happens if you input the guess '-5'?
  # Answer: print Too low!

# What happens if you input the guess '0'?
  # Answer: print Too low!

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: < means the value is undr the number, > means the value is over the numbet

# What happens if you change line 5 to if guess = number: ?
  # Answer : I would not work

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: there are comparing between the guess and number