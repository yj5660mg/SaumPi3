
#INSTRUCTIONS ABOUT THE GAME
#This game in Laotian is called : Saum Pi, translated into English : Three Cards.
#As many players as you would like, but here we chose 4.'
#The rule of the game is to score the Highest amount but only counting single digits, meaning if your card exceeds over 10 then you would get 1 for your cards adding up to 11.
#And face cards are counted as 10.  So Jack = 10, Queen = 10, King = 10.  For the Ace = 1.  The rest of the cards are just numbers.
#For example, an Ace, Jack, and Seven card would equal to being 18 in BlackJack, but in Three cards that would be 8, dropping the 10.
#So lets play!!



import random
import CardDeck
import PlayerClass
import FindWinner
# for uplead



numbers_used_list = []  # where used to try and make sure you don't draw the same card twice
def draw_cards():  # This function will add a random card

    rande_number = random.randint(1, 52)  # will pick a number from 0 to 52

    checker = True
    while checker == True:
        if rande_number not in numbers_used_list:  # checks if number in master list, so we don't get duplicate cards
            rando_card_num = CardDeck.numberMatchDictiony[rande_number]  # this works to return the card over the number
            numbers_used_list.append(rande_number)  # adding number to master list
            #print(numbers_used_list)  # used for testting to make sure no numbers are matching
            card_number_worth = CardDeck.cardDictiony[rande_number]  # will get the value of the card
            return rando_card_num, card_number_worth  # returning card type, and card playing value

        rande_number = random.randint(1, 52)  # will start over is number is in master list

# used to hold list of players cards
arrayPlayer1 = []
arrayPlayer2 = []
arrayPlayer3 = []
arrayPlayer4 = []

# used to hold list of player cards value
arrayPlayer1Numbers = []
arrayPlayer2Numbers = []
arrayPlayer3Numbers = []
arrayPlayer4Numbers = []

for x in range(3):
    card = draw_cards()
    arrayPlayer1.append(card[0])
    arrayPlayer1Numbers.append(card[1])
    #print(arrayPlayer1Numbers)   # used for data testing
    #print(total_score(arrayPlayer1Numbers))
    card2 = draw_cards()
    arrayPlayer2.append(card2[0])
    arrayPlayer2Numbers.append(card2[1])
    card3 = draw_cards()
    arrayPlayer3.append(card3[0])
    arrayPlayer3Numbers.append(card3[1])
    card4 = draw_cards()
    arrayPlayer4.append(card4[0])
    arrayPlayer4Numbers.append(card4[1])

# this list is used to determine whom wins the match
playerListNumbers = [FindWinner.total_score(arrayPlayer1Numbers), FindWinner.total_score(arrayPlayer2Numbers),
                     FindWinner.total_score(arrayPlayer3Numbers), FindWinner.total_score(arrayPlayer4Numbers)]



#Player = bob()
#bob = Player()
#bob.play()
#bob.play_winner()

print("Your cards are: ", arrayPlayer1, "Your score is: ", FindWinner.total_score(arrayPlayer1Numbers))  # not sure which looks better for viewing change how you wish lucky
print("Player two cards: ", arrayPlayer2, "score is: ", FindWinner.total_score(arrayPlayer2Numbers))
print("Player three cards: ")
print(arrayPlayer3, "score is: ", FindWinner.total_score(arrayPlayer3Numbers))
print("Player four cards: ")
print(arrayPlayer4, "score is: ", FindWinner.total_score(arrayPlayer4Numbers))
FindWinner.compare_score(playerListNumbers)


# billyBob = PlayerClass.Player("bob")
