import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# A deck as a sequence of cards
class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()				# split() creates a list

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
										for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	# __getitem__ delegates to the [] operator; allows for item access : deck[0]
	def __getitem__(self, position):
		return self._cards[position]

	# __setitem__ allows for item assignment : deck[2] = beer_card
	def __setitem__(self, position, other):
		self._cards[position] = other
	



beer_card = Card('7', 'diamonds')
beer_card

deck = FrenchDeck()
len(deck)			# => 52

# taking advantage of __getitem__ method:
deck[0]		# => Card(rank='2', suit='spades')
deck[-1]	# => Card(rank='A', suit='hearts')
