# Example code 1

number = 7 #a target
print("I have thought of a number between 1 and 10") #output
guess = int(input("Can you guess what it is?")) #the user would input his guessing

if guess == number: #guessing is equal to the target
  print("Correct!") # output
elif guess < number: #guessing is under the target
  print("Too Low!") #output
else: #anything besides the above
  print("Too High!") #ouput

# Example code 2

number1 = int(input("Please enter a number")) #user would input a number
number2 = int(input("Please enter another number")) #user would put another number

if number1 > number2: #number1 is over number2
  print("Number 1 is bigger than number 2")  #output
elif number2 > number1: #number2 Is over number 1
  print("Number 2 is bigger than number 1") #output
else: #anything besides above
  print("Both numbers are the same") #output 

