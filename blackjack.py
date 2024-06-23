import random

card_categories = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
card_list = ['Ace', '2','3', '4', '5', '6','7','8', '9', '10',
             'Jack','King','Queen']

deck = [(card, suit) for suit in card_categories for card in card_list]

def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])
    
#print(deck)
#print(type(deck))

#shuffle deck
random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

while True:
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in dealer_card)
    print("Cards Player Has:", player_card)
    print("Score Of The Player:", player_score)
    print("\n")
    choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
    if choice == "play":
        new_card = deck.pop()
        player_card.append(new_card)
    elif choice == "stop":
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    if player_score > 21:
        print("Cards Dealer Has:", dealer_card)
        print("Score Of The Dealer:", dealer_score)
        print("Cards Player Has:", player_card)
        print("Score Of The Player:", player_score)
        print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
        break
while dealer_score < 17:
    new_card = deck.pop()
    dealer_card.append(new_card)
    dealer_score += card_value(new_card)

print("Cards Dealer Has:", dealer_card)
print("Score Of The Dealer:", dealer_score)
print("\n")
