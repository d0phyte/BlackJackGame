import random


#BlackJackGame
#11 is the Ace card
#10 are the queen/king/jack and 10 cards
#Ace can also be 1 but for now will just use 11


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 

computerCards = []
userCards = []

#computerScore = 0
#userScore = 0

#This is the main game loop, after both the computer and user have drawn their first two cards 

def drawOneCard(computerScore, userScore):

    if computerScore == 21 and userScore == 21:
        print('It is a tie!')
        return
    elif computerScore == 21 and userScore < 21:
        print('The computer wins!')
        return
    elif userScore == 21 and computerScore < 21 :
        print('The user wins!')
        return
    elif computerScore > 21:
        print('The computer is over 21! It loses! ')
        return
    elif userScore > 21:
        print('The user is over 21. Game over !')
        return
    elif computerScore < 16:
        
        newCardComputer = random.choice(cards)
        computerCards.append(newCardComputer)
        computerScore = sum(computerCards)
        print(f'The computer score is lower than 16 so it draws an extra card.It draws a {newCardComputer} ')
        drawOneCard(computerScore, userScore)

    else:
    
        print(f'The computer has {computerScore} points and the user has {userScore} points.')
        hitOrStand = input('Do you want to hit or stand? Type "h" or "s": ')
        
        if hitOrStand == 'h':
            newDraw = random.choice(cards)
            userCards.append(newDraw)
            userScore = sum(userCards)
            print(f'The user draws a {newDraw}')
            print(f'The computer has {computerScore} points and the user has {userScore} points.')
            drawOneCard(computerScore, userScore)
        

        elif hitOrStand == 's':
            print(f'The computer has {computerScore} points and the user has {userScore} points.')
            if computerScore > userScore:
                print('The computer wins!')
                return
            elif userScore > computerScore:
                print('The user wins!')
                return
            else:
                print('It is a tie!')
                return
        
        else:
            print('Invalid input!')
            drawOneCard(computerScore, userScore)


#This is where the game starts and the first two cards are drawn for both the computer and the user

def gameStart():

    computerScore = 0
    userScore = 0
    computerFirstDraw = [random.choice(cards), random.choice(cards)]

    computerCards.append(computerFirstDraw[0])
    computerCards.append(computerFirstDraw[1])
    print(f'The computer draws a {computerFirstDraw[0]} and a {computerFirstDraw[1]}')
    computerScore = sum(computerCards)
    print(f'The computer score is {computerScore}')

    humanFirstDraw = [random.choice(cards), random.choice(cards)]
    userCards.append(humanFirstDraw[0])
    userCards.append(humanFirstDraw[1])
    print(f'The user draws a {humanFirstDraw[0]} and a {humanFirstDraw[1]}')
    userScore = sum(userCards)
    print(f'The user score is {userScore}')

    drawOneCard(computerScore, userScore)

    #if computerScore == 21 and userScore == 21:
        #print('It is a tie!')
        #return
    #elif computerScore == 21 and userScore < 21:
        #print('The computer wins!')
        #return
    #elif userScore == 21 and computerScore < 21 :
        #print('The user wins!')
        #return
    #elif computerScore > 21:
        #print('The computer loses!')
        #return
    #elif userScore > 21:
        #print('The user loses!')
        #return
    #elif computerScore < 16:
        
        #newCardComputer = random.choice(cards)
        #computerCards.append(newCardComputer)
        #computerScore = sum(computerCards)
        #print(f'The computer score is lower than 16 so it draws an extra card.It draws a {newCardComputer} ')
        #drawOneCard(computerScore, userScore)

    #else:
        #drawOneCard(computerScore, userScore)

gameStart()
            
        







