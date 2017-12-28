import random
result = "Hit or Stand? Press either h or s: "
playing = False  # indicates whether the player is playing or not
chip_pool = 100
bet = 1
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

suits = ('H','D','C','S') # heart, diamond, clubs, spades, THIS IS A LIST OF ALL POSSIBLE SUITS
ranking = ('A','2','3','4','5','6','7','8','9','10','J','Q','K') # possible card ranks THIS IS A LIST OF ALL POSSIBLE RANKING
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} #list of cards and their value

# a card class that has a suit and a rank
class Card(object) :

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return ( self.suit + self.rank)
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def draw(self):
        print (self.suit + self.rank)

#hand class that has a list of cards, a value in hand and finally a boolean value wether or not the hand contains an ace
class Hand(object):
    def __init__(self):
        self.cards = []
        self. value = 0
        self.ace = False
    def __str__(self):
        '''return a string of curent hand composition'''
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'the hand has %s' %(hand_comp)
    def card_add(self,card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]
    def calc_val(self):
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value
    def draw(self, hidden):
        if hidden == True and playing == True :
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()

# deck class
class Deck(object):

    def __init__(self):
        ''' Create a deck in order '''
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        ''' Shuffle the deck, python actually already has a shuffle method in its random lib '''
        random.shuffle(self.deck)

    def deal(self):
        ''' Grab the first item in the deck '''
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has" + deck_comp

# simply make a bet
def make_bet():
    ''' Ask the player for the bet amount and '''

    global bet

    print(' What amount of chips would you like to bet? (Enter whole integer please): ')
    while True:
        try:
            bet_comp = int(input())  # Use bet_comp as a checker
            # Check to make sure the bet is within the remaining amount of chips left.
            if bet_comp >= 1 and bet_comp <= chip_pool:
                bet = bet_comp
                break
            else:
                print("Invalid bet, you only have " + str(chip_pool) + " remaining")
                continue
        except :
            print('please enter a valid number.Try again ')
            continue

def deal_cards():
    # Set up all global variables
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    # Create a deck
    deck = Deck()

    # Shuffle the deck
    deck.shuffle()

    # Set up bet
    make_bet()

    # initialize both a playe hand and a dealer hand
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal out 2 cards each
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? Press either h or s: "
    if (playing == True): # if the player is indeed playing at the moment
        print('Fold, Sorry')
        chip_pool -= bet
    # Set up to know currently playing hand
    playing = True
    game_step()



def hit():
    ''' Implement the hit button '''
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    # If hand is in play add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print('---------------------------------------')
        print("Player hand is %s \n" % player_hand)

        if player_hand.calc_val() > 21:
            result = 'Busted! ' + restart_phrase

            chip_pool -= bet
            playing = False

    else:
        result = "Sorry, can't hit" + restart_phrase

    game_step()


def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet
    ''' This function will now play the dealers hand, since stand was chosen '''

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"

    # Now go through all the other possible options
    else:

        # Soft 17 rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        # Dealer Busts
        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts! You win!' + restart_phrase
            chip_pool += bet
            playing = False

        # Player has better hand than dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'You beat the dealer, you win!' + restart_phrase
            chip_pool += bet
            playing = False

        # Push
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Tied up, push!' + restart_phrase
            playing = False

        # Dealer beats player
        else:
            result = 'Dealer Wins!' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()


def game_step():
    'Function to print game step/status on output'

    # Display Player Hand
    print()
    print('Player Hand is: '),
    player_hand.draw(hidden=False)
    print('---------------------------------------')
    print('Player hand total is: ' + str(player_hand.calc_val()))
    print('---------------------------------------')
    # Display Dealer Hand
    print('Dealer Hand is: '),
    dealer_hand.draw(hidden=True)
    # If game round is over
    if playing == False:
        print(" --- for a total of " + str(dealer_hand.calc_val()))
        print("Chip Total: " + str(chip_pool))
    # Otherwise, don't know the second card yet
    else:
        print(" with another card hidden upside down")
    print('---------------------------------------')

    # Print result of hit or stand.
    print(result)
    player_input()
def game_exit():
    print ('Thanks for playing!')
    exit()


def player_input():
    ''' Read user input, lower case it just to be safe'''
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print("Invalid Input...Enter h, s, d, or q: ")
        player_input()

def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
Dealer hits until she reaches 17. Aces count as 1 or 11.
Card output goes a letter followed by a number of face notation'''
    print( statement)


# Create a Deck
deck = Deck()
#Shuffle it
deck.shuffle()
# Create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()
#Print the intro
intro()
print('\n')
# Deal out the cards and start the game!
deal_cards()

