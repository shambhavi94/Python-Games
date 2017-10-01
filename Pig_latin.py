def main():

	print ("Pig latin game.")
	print("")
	name = raw_input('Pleae enter your name: ')
	print 'Hello,', name, '! Welcome to pig latin game.'
	print("")
	vowels = ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U' )
	with_vowels = "yay"
	without_vowels = "ay"
	end = "Q", "q", "Quit", "quit"
	word = ""
	
	while (word != end):	
		word = raw_input('Please type what you would like to translate into pig latin or type Quit or q to quit and press enter: ')	
		
		if len(word) > 0 and word.isalpha() and word[0] in vowels and word != end:
			wordl = word.lower()
			new_word = wordl + with_vowels
			print(new_word)	
			 
			
			
		elif len(word) > 0 and word.isalpha() and word[0] not in vowels and word != end:	
			wordl = word.lower()
			new_word = wordl + wordl[0] + without_vowels
			new_word = new_word[1:]
			print(new_word)
						
		else:
			print "please enter a valid word/sentence"
		
			
	print("Thanks for playing pig latin! Hopefully will see you again")
	
main()
