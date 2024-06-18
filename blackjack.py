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
