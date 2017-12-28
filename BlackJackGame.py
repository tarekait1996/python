import random
# global variable that will be used

possible_suits = ('H','D','C','S')
possible_ranking = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
card_values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
is_playing = False
chip_pool = 100
bet = 0
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"
phrase = ''

class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit + self.rank
    def draw(self):
        print( self.suit , self.rank)
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank

class Hand(object):
    def __init__(self):
        self.cards = []
        self.value =0
        self.has_ace = False
    def __str__(self):
        all_cards_in_hand = ''
        for card in self.cards:
            card_name = card.__str__()
            all_cards_in_hand += " " + card_name
            return 'the hand has %s' % (all_cards_in_hand)
    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'A' and self.value < 12:
            self.value += 10
        else:
            self.value += card_values[card.rank]
    def draw(self, hidden):
        if hidden == True and is_playing == True :
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()
    def getValue(self):
        return self.value

class Deck(object):
    def __init__(self):
        self.deck = []
        # initialize the deck
        for suit in possible_suits:
            for rank in possible_ranking:
                self.deck.append(Card(suit,rank))
    def shuffle_deck(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
    def __str__(self):
        composition = ''
        for card in self.deck:
            composition += card.__str__ + ' '
        return composition

def make_a_bet():

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


# 4 choices, hit, stand, quit, deal
# 1 method for each

def deal():
    global bet, chip_pool,is_playing,dealer_hand,player_hand, phrase, deck

    # Create a deck
    deck = Deck()

    # Shuffle the deck
    deck.shuffle_deck()

    # Set up bet
    make_a_bet()

    # initialize both a playe hand and a dealer hand
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal out 2 cards each
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    phrase = "Hit or Stand? Press either h or s: "
    if (is_playing == True):  # if the player is indeed playing at the moment
        print('Fold, Sorry')
        chip_pool -= bet
    # Set up to know currently playing hand
    is_playing = True
    game()

def game():
    print()
    print('Player Hand is: '),
    player_hand.draw(hidden=False)
    print('---------------------------------------')
    print('Player hand total is: ' + str(player_hand.getValue()))
    print('---------------------------------------')
    # Display Dealer Hand
    print('Dealer Hand is: '),
    dealer_hand.draw(hidden=True)

    # If game round is over
    if is_playing == False:
        print(" --- for a total of " + str(dealer_hand.getValue()))
        print("Chip Total: " + str(chip_pool))
    # Otherwise, don't know the second card yet
    else:
        print(" with another card hidden upside down")
    print('---------------------------------------')
    print(phrase)
    player_input()


def hit():
    ''' Implement the hit button '''
    global is_playing, chip_pool, deck, player_hand, dealer_hand, phrase, bet

    # If hand is in play add card
    if is_playing:
        if player_hand.getValue() <= 21:
            player_hand.add_card(deck.deal())
        print('---------------------------------------')
        print("Player hand is %s \n" % player_hand)

        if player_hand.getValue() > 21:
            phrase = 'Busted! ' + restart_phrase

            chip_pool -= bet
            is_playing = False

    else:
        phrase = "Sorry, can't hit" + restart_phrase

    game()


def stand():
    global is_playing, chip_pool, deck, player_hand, dealer_hand, phrase, bet
    ''' This function will now play the dealers hand, since stand was chosen '''

    if is_playing == False:
        if player_hand.getValue() > 0:
            phrase = "Sorry, you can't stand!"

    # Now go through all the other possible options
    else:

        # Soft 17 rule
        while dealer_hand.getValue() < 17:
            dealer_hand.add_card(deck.deal())

        # Dealer Busts
        if dealer_hand.getValue() > 21:
            phrase = 'Dealer busts! You win!' + restart_phrase
            chip_pool += bet
            is_playing = False

        # Player has better hand than dealer
        elif dealer_hand.getValue() < player_hand.getValue():
            phrase = 'You beat the dealer, you win!' + restart_phrase
            chip_pool += bet
            is_playing = False

        # Push
        elif dealer_hand.getValue() == player_hand.getValue():
            phrase = 'Tied up, push!' + restart_phrase
            is_playing = False

        # Dealer beats player
        else:
            phrase = 'Dealer Wins!' + restart_phrase
            chip_pool -= bet
            is_playing = False
    game()

def player_input():
    ''' Read user input, lower case it just to be safe'''
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal()
    elif plin == 'q':
        game_exit()
    else:
        print("Invalid Input...Enter h, s, d, or q: ")
        player_input()


def game_exit():
    print('the program is now going to exit, thank you for playing!')
    exit(0)
deck = Deck()
dealer_hand = Hand()
player_hand = Hand()
#start the game
deal()