from collections import namedtuple

Card = namedtuple('Card', ['value', 'suit'])
as_spades = Card('A', 'Spades')
print(as_spades)
