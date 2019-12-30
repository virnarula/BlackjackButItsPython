import enum
import random

starting_money = 500
minimum_bet = 1
deck_size = 52


# @enum
class Suit(enum.Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4


# @enum
class Value(enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getName(self):
        return str(self.value) + " of " + str(self.suit)

    def __eq__(self, other):
        if self.suit == other.suit and self.value == other.value:
            return True
        return False


class Deck:
    def __init__(self, decks):
        self.deck = []
        self.decks = decks
        for i in range(0, decks):
            for suit in Suit:
                for value in Value:
                    self.deck.append(Card(suit, value))

    def draw(self):
        to_return = self.deck.pop()
        if len(self.deck) < 8:
            self.__init__(self.decks)
        return to_return

    def size(self):
        return len(self.deck)

    def swap(self, i, j):
        if i > self.size() - 1 or i < 0 or j > self.size() - 1 or j < 0:
            raise Exception("value was out of range")

        temp = self.deck[i]
        self.deck[i] = self.deck[j]
        self.deck[j] = temp

    def shuffle(self):
        j = 0
        deck_length = len(self.deck)
        for i in range(0, deck_length):
            j = random.randint(i, deck_length - 1)
            self.swap(i, j)

    def printDeck(self):
        for card in self.deck:
            print(card.getName())


def isBlackjack(hand):
    return False


def evaluateHand(hand):
    if isBlackjack(hand):
        return 22

    sum = 0
    aces = 0

    for card in hand:
        if card.getValue().value > 10:
            sum += 10
        elif card.getValue() == Value.ACE:
            sum += 1
            aces += 1
        else:
            sum += card.getValue().value

    while aces > 0 and sum <= 11:
        sum += 10
        aces -= 1

    if sum > 21:
        return -1

    return sum


class Round:
    def __init__(self, bet, player_cards, dealer_cards):
        self.bet = bet
        self.player_cards = player_cards
        self.dealer_cards = dealer_cards


class Game:
    def __init__(self, decks):
        self.decks = decks
        self.deck = Deck(decks)
        self.bet = 0
        self.money = starting_money
        self.starting_money = starting_money
        self.player_cards = []
        self.dealer_cards = []
        self.rounds = []

    def playGame(self):
        print("Starting game")
        self.deck.shuffle()
        while (self.money > 0):
            self.getBet()
            self.deal()
            self.getMove()
            self.clearHands()
            print("New round")

    def getBet(self):
        print("You have " + str(self.money))
        self.bet = int(input("Please enter your bet: "))
        while minimum_bet > self.bet or self.bet > self.money:
            self.bet = int(input("That was an invalid input. Try again: "))

    def getMove(self):
        user_in = 0
        while user_in != 2 and evaluateHand(self.player_cards) != -1:
            user_in = int(input("Please enter 1 to hit and 2 to stay:"))
            if user_in == 1:
                self.hit()
            elif user_in == 2:
                self.endRound()
            else:
                print("That was not a valid input. Try Again: ")

    def deal(self):
        self.dealer_cards.append(self.deck.draw())
        self.dealer_cards.append(self.deck.draw())
        print("The dealer shows a " + self.dealer_cards[0].getName())
        self.player_cards.append(self.deck.draw())
        self.player_cards.append(self.deck.draw())
        print("You got a " + self.player_cards[0].getName() + " and a " + self.player_cards[1].getName())

    def hit(self):
        self.player_cards.append(self.deck.draw())
        print("You got a " + self.player_cards[len(self.player_cards) - 1].getName())
        if evaluateHand(self.player_cards) < 0:
            self.endRound()

    def endRound(self):
        print("The dealer shows a " + self.dealer_cards[1].getName())
        while evaluateHand(self.dealer_cards) < 16 and evaluateHand(self.dealer_cards) != -1:
            self.dealer_cards.append(self.deck.draw())
            print("The dealer shows a " + self.dealer_cards[len(self.dealer_cards) - 1].getName())

        player_hand = evaluateHand(self.player_cards)
        dealer_hand = evaluateHand(self.dealer_cards)
        if player_hand > dealer_hand:
            print("You won the round")
            self.money += self.bet
        elif player_hand < dealer_hand:
            print("You lost the round")
            self.money -= self.bet
        else:
            print("It was a tie")

        self.rounds.append(Round(self.bet, self.player_cards, self.dealer_cards))

    def clearHands(self):
        self.player_cards.clear()
        self.dealer_cards.clear()
        self.bet = 0
