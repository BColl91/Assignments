# The Cards Module

import sys

class Card(object):
	CARDS=["2", "3", "4", "5", "6", "7", "8", "9", "10",
			"Jack", "Queen", "King", "Ace" ]
	SUITS=[ "Clubs", "Diamonds", "Hearts", "Spades"]
	def __init__(self, card, suit, face_up = True):
		self.card = card
		self.suit = suit
		self.is_face_up = face_up
	def __str__(self):
		if self.is_face_up:
			rep = self.card + " of " + self.suit
		else:
			rep = "XXX of XXXXXX"
		return rep

	def flip(self):
		self.is_face_up = not self.is_face_up
		
class Hand(object):
	def __init__(self):
		self.cards = []
	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + "; "
		else:
			rep = "<empty>"
		return rep
	def clear(self):
		self.cards = []
	def add(self, card):
		self.cards.append(card)
	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)

class Deck(Hand):
	def populate(self):
		for suit in Card.SUITS:
			for card in Card.CARDS:
				self.add(Card(card, suit))
	def shuffle(self):
		import random
		random.shuffle(self.cards)
	def deal(self, hands, per_hand = 1):
		for rounds in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card = self.cards[0]
					self.give(top_card, hand)
				else:
					print("Deck has run out of cards. Game over.")
					sys.exit()
if __name__ == "__main__":
	print("This is a module with classes for playing cards.")
	input("\nPress Enter to exit.")
		