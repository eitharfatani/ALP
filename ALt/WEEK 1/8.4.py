'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''
weap = ["gun", "fire", "RPG", "knife"]
zombieWeakness = weap[0]
print ("There is a zombie, start fighting!")

choice = (input(str(weap)+"Do you want to use weapon from the list (type A), or use your own weapon (type B) ?"))

if choice == "A":
  print("Enter the the weapon index")
  index = int(input())
  while index != 0:
  
    print("You did not win try agian. Enter the the weapon index")
    index = int(input())
    print(weap[index])

elif choice == "B":
  newitem= input("Enter a weaopon-  ")
  weap.append(newitem)
  print(weap)
  print("Enter the the weapon index")
  index = int(input())
  while index != 0:
    print("Enter the the weapon index")
    index = int(input())
    print(weap[index])

else:
  print("Error")

print("Congratulations You Won!")