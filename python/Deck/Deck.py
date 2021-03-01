class Deck:

	def __init__(self, size):
		self.size = size
		self.cards = []

	def addCard(self, card):
		if len(self.cards) < self.size:
			self.cards.append(card)
		else:
			print("Deck is full!")

	def size(self):
		return len(self.cards)
