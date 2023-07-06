def add_calc(num1, num2):
  return num1 + num2
def subtract_calc(num1, num2):
  return num1 - num2
def multiply_calc(num1, num2):
  return num1 * num2
def divide_calc(num1, num2):
  return num1 / num2

num1 = int(input("enter a number"))
num2 = int(input("enter another number"))

print ("1. add")
print ("2. subtract")
print("3. multiply")
print("4. divide")
choice = input("Choose one of the operations:")

if choice == "1":
  outputNum= add_calc(num1, num2)
  print (outputNum)
  print (str(num1) + " + " + str(num2) + " = " + str(outputNum))

elif choice == "2":
  outputNum= subtract_calc(num1, num2)
  print (outputNum)
  print (str(num1) + " - " + str(num2) + " = " + str(outputNum))

elif choice == "3":
  outputNum= multiply_calc(num1, num2)
  print (outputNum)
  print (str(num1) + " * " + str(num2) + " = " + str(outputNum))

elif choice == "4":
  outputNum= divide_calc(num1, num2)
  print (outputNum)
  print (str(num1) + " / " + str(num2) + " = " + str(outputNum))

else:
  print ("Erorr")
