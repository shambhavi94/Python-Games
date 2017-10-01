print("Welcome to Montek's Dungeon!")
command= ""
while command!="q":
	command=raw_input('You are in the kitchen.There are doors to the west(w), south(s) and east(e). ' )
	room= "K"
	if command== "s" and room=="K":
		print("You entered the furnace and fry yourself to death!")
		command="q"
		
	elif command=="e" and room=="K":
		room="LR"
		command=raw_input("You are in the living room. No sign of the Princess. There are doors to the west(w)." )
		if command=="w" and room=="LR":
			room="K"
	         
	elif command=="w" and room=="K":
		room="H"
		command=raw_input("You are in the hallway. There are doors to the south(s) and east(e). ")
		if command=="e" and room=="H":
			room= "K"
			
		elif command=="s" and room=="H":
			print("You are in the library. You found the Princess! You are a hero!")
			command="q"

print("Good bye!")
