import random

def diceroll():
	#rolling of dice by the randint function
	roll=random.randint(1,6)
	return roll
	
def ladder(player):
	#checking the ladder condition
	dic1= {1:38, 4:14, 8:30, 21:42, 50:67,  71:92}
	if player in dic1.keys():
		player = dic1[player]
		print('you got a ladder')
	else:
		player= player
	return player

def snake(player):
	#checking the snake condition
	dic2={32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:3}
	if player in dic2.keys():
		player= dic2[player]
		print('You got bit by a snake.')
	else:
		player=player
	return player
	
def advance(player):
	#moving forward on the board
	while(player<=100):
		n=int(input())
		if (n==0):
			print('You quit.')
			print('Your position --> {}'.format(player))
			return player
		x=diceroll()
		print('Your position --> {}'.format(player))
		print('Your roll--> {}'.format(x))
		print('')
		player += x
		player = ladder(player)
		player = snake(player)
		
	player -=x
	while(player!=100):
		#the curious case of final 90's number
		n=int(input())
		x=diceroll()
		req = 100-player
		if(x<=req):
			player += x
			print('Your position --> {}'.format(player))
			print('Your roll --> {}'.format(x))
			
		else:
			print('Your position--> {}'.format(player))
			print('Your roll --> {}'.format(x)) 
			
		return player


#MAIN
print('Lets play Snakes and Ladders!!!!!')
print('Rules are quite simple. Enter any number to roll the dice. Your position will advance in accordance. At certain steps, there are ladders to escalate your movement.')
print('And some snakes too, obviously. They could bring you down badly.')
print('When you reach 100, you will win!')
print('If you want to quit, enter 0.')	
player=0
player= advance(player)
			
if (player==100):
	#to check the win
	print('you won!!!')
	
	
	
