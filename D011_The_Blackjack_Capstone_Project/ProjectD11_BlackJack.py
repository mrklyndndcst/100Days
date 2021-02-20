#done first 2 cards of the player
#done convert A and jack to king to integers then sum
#done make a lost print if exceeded to 21 for player
#add dealer show first card
#
import random
import time
deck = [
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
   ]

dealer_card = []    #card on hand of the dealer
dealer_total = 0
player_card = []    #card on hand of the player
player_pick = 2     #card to pick of the player

while player_pick != 0:

    if player_pick == 2:
        card = random.randint(0,len(deck)-1)
        dealer = deck[card]
        print(f"Dealer picked {dealer}")
        del deck[card]
        dealer_card.append(dealer)

    time.sleep(1)

    card = random.randint(0,len(deck)-1)
    player = deck[card]
    print(f"Player picked {player}")
    del deck[card]
    player_pick -= 1
    player_card.append(player)

    if player_pick == 0:
        player_total = 0
        for to_add in player_card:
            if to_add != "A":
                if to_add != "J":
                    if to_add != "Q":
                        if to_add != "K":
                            player_total += int(to_add)
            if to_add == "J" or to_add == "Q" or to_add == "K" :
                player_total += 10
        for add_a in player_card:        
            if add_a == "A":
                if player_total + 11 > 21:
                    player_total += 1
                elif player_total + 11 <= 21:
                    player_total += 11
    time.sleep(1)
    if player_pick == 0:
        if player_total > 21:
            print(f"The Player have {player_total} BUSTS")
            print("Dealer Wins!!!")
        elif player_total == 21 and len(player_card) == 2 and int in dealer_card and dealer_card != 10:
            print(f"You have {player_card} BLACKJACK")
            print("Player Wins!!!")
        elif player_total == 21 and len(player_card) == 2 and str in dealer_card and dealer_card == 10:
            
            card = random.randint(0,len(deck)-1)
            dealer = deck[card]
            print(f"Dealer picked {dealer}")
            del deck[card]
            dealer_card.append(dealer)    

            for to_add in dealer_card:
                if to_add != "A":
                    if to_add != "J":
                        if to_add != "Q":
                            if to_add != "K":
                                dealer_total += int(to_add)
                if to_add == "J" or to_add == "Q" or to_add == "K" :
                    dealer_total += 10
            for add_a in dealer_card:        
                if add_a == "A":
                    if dealer_total + 11 > 21:
                        dealer_total += 1
                    elif dealer_total + 11 <= 21:
                        dealer_total += 11

            if dealer_total == 21:
                print("The Player and The dealer each have Blackjack the result is a PUSH.")
            else:
                print(f"Player have {player_card} BLACKJACK")
                print("Player Wins!!!")
        elif player_total <= 21:
            print(f"Player have {player_card} total of {player_total}")
            hit = input("type 'hit' for HIT and 'stand' for STAND: ")
            if hit == "hit":
                player_pick += 1
            else:
                
                while dealer_total < 17:

                    time.sleep(1)

                    card = random.randint(0,len(deck)-1)
                    dealer = deck[card]
                    print(f"Dealer picked {dealer}")
                    del deck[card]
                    dealer_card.append(dealer)    

                    dealer_total = 0

                    for to_add in dealer_card:
                        if to_add != "A":
                            if to_add != "J":
                                if to_add != "Q":
                                    if to_add != "K":
                                        dealer_total += int(to_add)
                        if to_add == "J" or to_add == "Q" or to_add == "K" :
                            dealer_total += 10
                    for add_a in dealer_card:        
                        if add_a == "A":
                            if dealer_total + 11 > 21:
                                dealer_total += 1
                            elif dealer_total + 11 <= 21:
                                dealer_total += 11  
                if dealer_total > 21:
                    print(f"The Dealer have {dealer_total} BUSTS")
                    print("Player Wins!!!")
                elif dealer_total > player_total:
                    print(f"Player have lower hand {player_card} total of {player_total}")
                    print(f"Dealer have higher hand {dealer_card} total of {dealer_total}")
                    print("Dealer Wins!!!")
                elif dealer_total < player_total:
                    print(f"Dealer have higher hand {dealer_card} total of {dealer_total}")
                    print(f"Player have lower hand {player_card} total of {player_total}")
                    print("Player Wins!!!")
                else:
                    print(f"Player have {player_card} total of {player_total}")
                    print(f"Dealer have {dealer_card} total of {dealer_total}")
                    print("The Player and The dealer have same value NO ONE WINS.")






##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

