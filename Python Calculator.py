#Made by P-XXXVII
import os
import time
import sys

try:
	input = raw_input
except NameError:
	pass


def clear_term():
	os.system('clear')


#Cores=============================================================================================================================================

def add(num1,num2): #Core-Add
	answer =  int(num1) + int(num2)
	return answer 

def multiply(num1,num2): #Core-Multiply
	answer =  int(num1) * int(num2)
	return answer 

def subtraction(num2,num1): #Core-Subtraction
	answer =  int(num2) - int(num1)
	return answer 

def division(num1,num2): #Core-Division
	answer =  int(num2) / int(num1)
	return answer 


#Mods===============================================================================================================================================

def inputadd(): #Extra cal input
	while True:

		number1 = input("Addend1:")
		if number1.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue
		else:
			pass

		number2 = input("Addend2:")
		if number2.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue

		else:
			print("Your sum is: "+str(add(number1,number2)))
			break

def inputmultiply(): #Extra cal input
	while True:

		number1 = input("Factor1:")
		if number1.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue
		else:
			pass

		number2 = input("Factor2:")
		if number2.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue

		else:
			print("Your product is: " +str(multiply(number1,number2)))
			break

def inputsubtraction(): #Extra cal input
	while True:
		number2 = input("Minuend:")
		if number2.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue
		else:
			pass

		number1 = input("Subtrahend:")
		if number1.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue

		else:
			print("Your sum is: "+str(subtraction(number2,number1)))
			break

def inputdivision(): #Extra cal input
	while True:

		number1 = input("Dividend:")
		if number1.isdigit() == False:
			print("You can only enter numbers, Restart.")
			time.sleep(1)
			continue
		else:
			pass

		number2 = input("Divisor:")
		if number2.isdigit() == False:
			print("You can only enter numbers, Restart")
			time.sleep(1)
			continue

		else:
			print("Your Quotient is: "+str(division(number2,number1)))
			break

#Control==============================================================================================================================================

def user_choice(): #User Control
	choice_user = input("Please select one of the following.\n (Add,Multiply,Subtraction,Division or Quit)\n>>>:")
	choice_user = choice_user.lower()
	if choice_user == 'add':
		inputadd()
		time.sleep(3)
		clear_term()
	elif choice_user == 'multiply':
		inputmultiply()
		time.sleep(3)
		clear_term()
	elif choice_user == 'subtraction':
		inputsubtraction()
		time.sleep(3)
		clear_term()
	elif choice_user == 'division':
		inputdivision()
		time.sleep(3)
		clear_term()
	elif choice_user == 'quit':
		print('Quitting')
		time.sleep(1)
		clear_term()
		sys.exit()

	else:
		print('nigga u dumb, pick one of them.')

#Start Calling========================================================================================================================================
		
	


clear_term()
print('Do not intrust your exams with this\n')

while True:
	user_choice()

clear_term()
user_choice()