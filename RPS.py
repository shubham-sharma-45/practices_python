from math import ceil

def rps() : 
	global count_player_1,count_player_2
	print("Enter R for Rock, P for Paper and S for Scissor")
	player1 = input("Enter Choice for Player 1 : ")
	player2 = input("Enter Choice for Player 2 : ")

	if player1 == "R" : 
		if player2 == "R" :
			print("Its a Draw")
			#return 
		elif player2 == "P" :
			print("player2 Wins")
			count_player_2 +=1
			#return
		elif player2 == "S" :
			print("Player1 Wins")
			count_player_1 +=1
		else : 
			print("Invalid Choice")

	elif player1 == "P" : 
		if player2 == "P" :
			print("Its a Draw")
			#return 
		elif player2 == "S" :
			print("player2 Wins")
			count_player_2 +=1
			#return
		elif player2 == "R" :
			print("Player1 Wins")
			count_player_1 +=1
		else : 
			print("Invalid Choice")


	elif player1 == "S" : 
		if player2 == "S" :
			print("Its a Draw")
			#return 
		elif player2 == "R" :
			print("player2 Wins")
			count_player_2 +=1
			#return
		elif player2 == "P" :
			print("Player1 Wins")
			count_player_1 +=1
		else : 
			print("Invalid Choice")

count_player_1 = 0
count_player_2 = 0
count_total = int(input("Enter the Number of Iteration : "))

for i in range(count_total) : 
	rps()
	if count_player_1 > ceil(count_total/2) or count_player_2 > ceil(count_total/2) :
		break

if count_player_2 > count_player_1 :
	print("Player 2 Wins the Game")
elif count_player_2 == count_player_1 : 
	print("Draw")
else : 
	print("Player 1 Wins the Game")
