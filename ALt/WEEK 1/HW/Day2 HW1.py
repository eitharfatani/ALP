'''
Task Instructions
You are going to write a program called "Time Reminder"

The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up" #
If the number is less than 12 display a message saying "Good morning"#
If the number is less than 14 display a message saying "Lunch time!"#
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less than 19 display a message saying "Good evening"
If the number is less than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognise that”


You are free to use any of the methods that we have learned in class.
'''
#Start coding below this line

#Time Reminder

time = int(input("Hello, choose a time between 0 and 23: "))
if time < 8:
  print("too early to get up")

elif 8 <= time < 12:
  print("good morning")

elif 12 < time < 14:
  print("lunch time!")

elif 14 <= time < 18:
  print("good afternoon!")

elif 18 <= time < 19:
  print("good evening!")

elif 19 <= time < 22:
  print("nearly bedtime")

elif time == 23:
  print("good night!")

else:
  print("Sorry, I don’t recognise that")


