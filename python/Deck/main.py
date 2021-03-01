import Deck
import Card

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
cards = []

for i in range(1, 53, 1):
	cards[i] = Card("", "")
	print(cards[i])

# print(len(ranks))
# print(suits)
