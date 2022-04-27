from DeckOfCards import DeckOfCards
import random

print("Welcome to Black Jack!")
print()

score = 0

while score >= 0: # loops through the game until user ends it

    # print deck
    
    print("Deck before shuffled: ") 
    deck = DeckOfCards()
    deck.print_deck() 
    print()
    
    # print shuffled deck
    
    print("Deck after shuffled: ")
    deck.shuffle_deck()
    deck.print_deck()
    
    # deal card 1 & 2
    
    card1 = deck.deal_card()
    print("Card One: ", card1)
    
    card2 = deck.deal_card()
    print("Card Two: ", card2)
    
    # calculate user's hand score and dealer score
    
    score = 0
    dealer_score = random.randint(17,23)
    
    score += card1.val 
    score += card2.val
    print("Your total score is: ", score)
    if score == 21: 
        if dealer_score < 21 or dealer_score > 21:
            print("Blackjack, you win!")
        if dealer_score == 21:
            print("Dealer score: ", dealer_score)
            print("It's a tie!")
        break
    
    # continue dealing cards to the user while they ask for a ‘hit’, or until the total value of their cards exceeds 21
    
    while score < 21:
        hit = input("Would you like a hit? (y/n): ")
        if hit == "y":
            new_card = deck.deal_card()
            print("New card: ", new_card)
            score += new_card.val #adds card value to count total score
            print("Your total score is: ", score)
            
            if score == 21:
                print("Score is 21, you win!")
                break
            
            if score > 21:
                print("Bust, you lose!")
                break

        else: # aka user does not ask for hit  
            print("Dealer score is: ", dealer_score)
            if dealer_score > 21:
                print("Dealer busts, you win!")
                break
            if score > dealer_score and score <= 21:
                print("Dealer score is lower, you win!")
                break
            if dealer_score > score:
                print("Dealer score is higher, you lose!")
                break
            if score == 21:
                print("Score is 21, you win!")
                break
            if dealer_score == score:
                print("Dealer score: ", dealer_score)
                print("It's a tie!")
        
    new = input("Play again? (y/n): ") #asks user if they want to play again (if not, ends game)   
    if new == "y":
        print()
        continue
    if new == "n":
        score = -1
        print("Game over")
