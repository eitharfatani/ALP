# Example Code 1

def say_hi(): #subroutine 1
  print("Why hello there!") 

def offer_drink(): #subroutine 2
  print("Would you care for a spot of tea?")

def offer_food(): #subroutine 3
  print("Biscuit?")

def say_bye(): #subroutine 4
  print("Cheerio then.")


offer_drink() #calling subroutine 2 
say_hi() #calling subroutine 1
offer_food() #calling subroutine 3

# Example code 2
def maths1(): #subroutine 1
  num1 = 50 #variable
  num2 = 5 #variable
  return num1 + num2 #add num1 to num2

def maths2(): #subroutine 2
  num1 = 50 #variable
  num2 = 5 #variable
  return num1 - num2 #subtract num2 from num1

def maths3(): #subroutine 3
  num1 = 50 #variable
  num2 = 5 #variable
  return num1 * num2 #multiply num1 by num2

outputNum = maths2() #variable store def maths2() 
print(outputNum) #it would print the answer

# Example Code 3
def location(country): #subroutine with argument
  print("I am from " + country) #output


location("Brazil") #print the statement with Brazil

