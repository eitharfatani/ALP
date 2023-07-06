'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.#
2. Greet the user by name.#
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''
#1
name= input("What is your name? ")

#2
print ("Nice to meet you "+name+"!")

#3 + 4
country=input("Where are you from? ")
print(country+" is an amazing coountry, "+name+"!")

color = input("What is your favourite color? ")
print("What a beautiful color, " + name +"! "+ "I like "+ color+" too")

friend = input("Do you want to be my friend?")
print("Nice, "+name+"!")

#5 
print("Now I have Known that your name is "+(name)+ ",you are from " + country +",you like "+ color+", and I think we are freinds because you said "+friend+", Let's have fun together!")







