import random


#BlackJackGame
#11 is the Ace card
#10 are the queen/king/jack and 10 cards
#Ace can also be 1 but for now will just use 11

#There is a bug where if the computer gets 21 it wins before the user can draw a card: fixed
#Bug where if the user stands, if the computer is not over 16 the last card is not added to the sum: fixed
#If the user has 21 points he should not be able to draw another card (should automatically stand): not fixed yet

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 

computerCards = []
userCards = []

#computerScore = 0
#userScore = 0

#This function is called at the end of the game to see if the user wants to play again

def playAgain():
    playAgain = input('Do you want to play again? Type "y" or "n": ')
    if playAgain == 'y':
        computerCards.clear()
        userCards.clear()
        gameStart()
    elif playAgain == 'n':
        print('Thanks for playing!')
        return
    else:
        print('Invalid input! Stopping game!')

        return
        
        


#The computer is forced to draw until its score is over 16

def checkComputerOver16(computerScore, userScore):
    i = 0
    while computerScore < 16:
        i += 1
        newCardComputer = random.choice(cards)
        computerCards.append(newCardComputer)
        computerScore = sum(computerCards)
        print(f'The computer draws a {newCardComputer} ')
    
    if i == 0:
        #print('The computer did not draw any extra cards because it was already over 16 points.')
        return computerScore
    else:
        print(f'The computer drew {i} extra cards.')
        return computerScore
        


#This is the main game loop, after both the computer and user have drawn their first two cards 

def checkWinner(computerScore, userScore):
    
        if computerScore == 21 and userScore == 21:
            print('It is a tie!')
            playAgain()
            return 
        elif computerScore == 21 and userScore < 21:
            print('The computer wins!')
            playAgain()
            return
        elif userScore == 21 and computerScore < 21 :
            print('The user wins!')
            playAgain()
            return
        elif computerScore > 21:
            print('The computer is over 21! It loses! ')
            playAgain()
            return
        elif userScore > 21:
            print('The user is over 21! It loses!')
            playAgain() 
            return
        elif computerScore > userScore:
            print('The computer wins!')
            playAgain()
            return
        elif userScore > computerScore:
            print('The user wins!')
            playAgain()
            return
        elif computerScore == userScore:
            print('It is a tie!')
            playAgain() 
            return
        
        else:
            drawOneCard(computerScore, userScore)
            return

def drawOneCard(computerScore, userScore):

    #checkWinner(computerScore, userScore)

    if userScore < 22:
      

        hitOrStand = input('Do you want to hit or stand? Type "h" or "s": ')
        
        if hitOrStand == 'h':
            print('The user hits!')
            newDraw = random.choice(cards)
            userCards.append(newDraw)
            userScore = sum(userCards)
            print(f'The user draws a {newDraw}')
            print(f'The computer has {computerScore} points and the user has {userScore} points.')
            drawOneCard(computerScore, userScore)
            

        elif hitOrStand == 's':
            print('The user stands!')
            computerScore = checkComputerOver16(computerScore, userScore)
            print(f'The computer has {computerScore} points and the user has {userScore} points.')
            checkWinner(computerScore, userScore)
            
            
            
        
        else:
            print('Invalid input! Try again!')
            drawOneCard(computerScore, userScore)
    else:
        print('The user is over 21! Game Over!')
        playAgain()
        return



#This is where the game starts and the first two cards are drawn for both the computer and the user

def gameStart():

    computerScore = 0
    userScore = 0
    computerFirstDraw = [random.choice(cards), random.choice(cards)]

    computerCards.append(computerFirstDraw[0])
    computerCards.append(computerFirstDraw[1])
    
    computerScore = sum(computerCards)
    print(f'The computer draws a {computerFirstDraw[0]} and a {computerFirstDraw[1]}')
    print(f'The computer score is {computerScore}')

    humanFirstDraw = [random.choice(cards), random.choice(cards)]
    userCards.append(humanFirstDraw[0])
    userCards.append(humanFirstDraw[1])
    
    userScore = sum(userCards)
    print(f'The user draws a {humanFirstDraw[0]} and a {humanFirstDraw[1]}')
    print(f'The user score is {userScore}')

    drawOneCard(computerScore, userScore)


gameStart()


            
       






