# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?") #input
answer = input() 

while answer != "Paris": #answer is not equal to "Paris"
  print("Incorrect! Try again.") #print statement
  answer = input("What is the capital of France?") #ask again 

print("Correct!") #answer is Paris, so print "Correct"

# Example code 2

counter = 1 #vaianble stores value 1

while counter < 5: #variable is loweth than 5
  print("This code is inside the loop") #print statement
  counter += 1 #add 1 to 5 and check again of counter is less than 5 or not, If yes, the statement would be printed