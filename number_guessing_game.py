#number guessing game 
import random as r
Player=input("Choose player name: ")
print("Hi",Player," welcome to (NUMBER GUESSING GAME)")

print("**GAME IS START**")
	
User=int(input("Enter number: "))
print("your points: ",User)
computer=r.randint(1,100)
print("computerbot: ",computer)
if User > computer:
	print("you win!!")
else:
	print("you lose!!")
	 
print("Thank you for playing this game!!")
