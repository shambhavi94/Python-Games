import Tkinter as tk  # use tk namespace for Tkinter items
import random

def main():
	print (" welcome to the dice rolling")
	print ("")
	end_program = 0
	while end_program != "q" or "Q" or "Quit" or "quit":
		print (" Please press enter to roll the dice or q to quit")
		raw_input()
		number = random.randint(1,6)
		
		if number == 1:
			print("-------")
			print ("  O")
			print("-------")
			print("1")
			end_program = raw_input()
		elif number == 2:
			print("-------")
			print (" O O")
			print("-------")
			print("2")
			end_program = raw_input()
		elif number == 3:
			print("-------")
			print ("  O ")
			print (" O O")
			print("-------")
			print("3")
			end_program = raw_input()
		
		elif number == 4:
			print("-------")
			print (" O O")
			print (" O O")
			print("-------")
			print("4")
			end_program = raw_input()
		
		elif number == 5:
			print("-------")
			print (" O O")
			print ("  O ")
			print (" O O")
			print("-------")
			print("5")
			end_program = raw_input()
		
		elif number == 6:
			print("-------")
			print (" O O")
			print (" O O")
			print (" O O")
			print("-------")
			print("6")
			end_program = raw_input()
						
main()
