import random

print('***Welcome to Rock , Paper , Scissors Game***')

randomNumber = random.randint(0, 2)

player1_point = 0
player2_point = 0
winner_point = 4

if randomNumber == 0 :
    computerMove = "rock"
elif randomNumber == 1 :
    computerMove = "paper"
elif randomNumber == 2 :
    computerMove = "scissors"    



while(player1_point < winner_point and player2_point < winner_point) :

    print('----------------------------------')
    print("Player 1 point : " + str(player1_point))
    print("Player 2 point : " + str(player2_point))
    print('----------------------------------')
    Player1 = input("Player 1,make your move : ")
    Player2 = computerMove 
    print("Computer move : " + computerMove)

    if Player1 == Player2 :
        print('thats a tie')
    elif Player1 == "rock" :
        if Player2 == "scissors" :
            print('Player 1 wins!...')
            player1_point += 1
        elif Player2 == "paper" :
            print('Player 2 wins!...')
            player2_point += 1
    elif Player1 == "paper" :
        if Player2 == "scissors" :
            print('Player 2 wins!...')
            player2_point += 1
        elif Player2 == "rock" :
            print('Player 1 wins!...')
            player1_point += 1 
    elif Player1 == "scissors" :
        if Player2 == "rock" :
            print('Player 2 wins!...')
            player2_point += 1
        elif Player2 == "paper" :
            print('Player 1 wins!...') 
            player1_point += 1
    else :
        print('something was wrong!!!')

print("Final Scores \n Player 1 : " + str(player1_point) + "| Player 2 : " + str(player2_point))
