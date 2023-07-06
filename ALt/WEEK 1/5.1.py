'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1

age = 18 
#variable (age) stores the value 18
if age > 18: #the program would check if the value is over 18, if yes, it will print the statement
 print("You are old enough to drive") 

# Example code 2

num1 = 1337 
#variable (num1) stores the value 1337

if num1 == 10: #the program would check if the value is equale to 10, if yes, it will print the statement
  print("This text is output because the condition was true") 
else: #the program would check if the value is equale to 10, if no, it will print the statement
  print("This text is output because the condition was false") 

# Example code 3

number = 5 #variable (number) stores the value 1337
print("I have thought of a number between 1 and 10") 
guess = int(input("Can you guess what it is?")) #the user would input the guessing

if guess == number: #the program would check if the value is equale to variable (number), if yes, it will print the statement
  print("This text is output because the")
  print("Correct!")
if guess < number: #the program would check if the value is under variable (number), if yes, it will print the statement
  print("Too Low!")
if guess > number: #the program would check if the value is over variable (number), if yes, it will print the statement
  print("Too High!")