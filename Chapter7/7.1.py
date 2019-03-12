#Deck of Cards:
#Design the data structures for a generic deck of cards.
#Explain how you would subclass the data structures to implement blackjack.


import random

class Card():

    #class attributes
    suit_names = ['Club','Diamond','Heart','Spade']
    rank_names = ["None","Ace","2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King"]

    # instance attributes
    def __init__(self,suit = 0,rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def get_value(self):
        return self.suit

class Deck():

    #create deck of 52 cards
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.card.append(card)

    #To print the Deck
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " " + res

    def remove_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle_cards(self):
        return self.cards.shuffle()

    def sort_carts(self):
        return sorted(self.cards)

    def remaining_cards(self):
        return len(self.cards)

class Game():
    def __init__(self):
        self.hands = []

    def deal_hand(self):
        for people in range(4):
            hand = Hand()
            self.hands.append(hand)

            for i in range(5):
                x = random.randint(len(self.cards))
                hand.cards.append(self.cards[x])

    def play(self):
        winner = self.hands[0]
        for i in range(len(self.hands)-1):
            if self.hands[i].score() > self.hands[i+1].score():
                winner = self.hands[i]
        return winner
    def deal_card(self):
        pass

class Hand():

    def __init__(self):
        self.cards = []

    def score(self):
        score = 0
        for card in self.cards:
            score += card.get_value()
        return score

    def add_card(self,card):
        self.cards.append(card)



if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    game = Game()
    game.play()
