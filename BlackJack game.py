from decimal import DecimalException
import random
playerIn = True
dealerIn = True

#deck of cards/player hand and dealers hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A',  'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

#deal the cards
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calulate the total of each hand 
def total(turn):
    total  = 0
    face = ['J', 'Q', 'K', 'A']
    for card in turn:
        if card in range(1, 11):
            total += card 
        elif card in face:
            total += 10 
        else:
            if total > 11:
                total += 1 
            else:
                total += 11       
    return total

#check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand [0]
    elif len(dealerHand) > 2:
        return dealerHand [0], dealerHand[1]

#game loop
for _  in range(2):
    dealcard(dealerHand)
    dealcard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X") 
    print(f"You have {playerHand} for a total of {total(playerHand)}") 
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealcard(dealerHand)
    if stayOrHit == '1':
        playerIn == False 
    else:
        dealcard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

#Winning screen 
if total(playerHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Blackjack You Win!")
elif total(dealerHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("BlackJack Dealer Win!")
elif total(playerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("you bust! Dealer Wins!")
elif total(dealerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("dealer bust! you win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Dealer Win!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("You Win!")
elif total(dealerHand) > total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("You Win!")
elif total(dealerHand) < total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Dealer Win!")
elif total(dealerHand) == total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Tie!")
