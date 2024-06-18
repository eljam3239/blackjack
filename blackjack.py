import random

card_categories = ['Hearts', 'Diamonds', 'Spades', 'Cluns']
card_list = ['Ace', '2','3', '4', '5', '6','7','8', '9', '10'
             'Jack','King','Queen']

deck = [(card, suit) for suit in card_categories for card in card_list]

