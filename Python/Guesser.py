import random
#The program randomly generates a positive integer up to 100, then gives the user up to five chances to guess the generated number. 

replay = "yes"
while replay == "yes":
	strikes = 0
	# Asks for guess & adds up until you've hit 5 strikes.
	while strikes < 5:
		random_number = random.randint(1,100)
		guess = int(input("What number am I thinking of? "))
		#Need to figure out error traps & raise an exception
		if guess != random_number:
			strikes = 1 + strikes
		elif guess == random_number:
			print("You won in ", strikes+1, "attempt(s)! Good job!")
	#Now that the player is out of chances to guess, the program is telling the player that they lost, and what the answer was.
	#Furthermore, if they player wants to play again, they have the option. This will use the first while in order to start again.
	while strikes == 5:
		print("Sorry, it seems you lost... the number was", random_number)
		replay = input("Would you like to play again?(yes/no) ").lower()
		if replay == "yes":
			strikes = 0
		elif replay == "no":
			print("Have a good day!")
		else:
			print("Hey there Delilah, what's it like in New York City?")#Raise an exception here too if the player doesn't give a legitimate input.