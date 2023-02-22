import random
import streamlit as st
import os

st.set_page_config(page_title="POKER Probability", initial_sidebar_state="collapsed")

path = os.path.dirname(__file__)
css = path + '/style.css'

with open(css) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Given a list hand containing five strings being the cards, implement a function that returns a string with the name of the highest combination obtained, accordingly to the table above.

cards = []
# testing = ["1_C", "10_C", "11_C", "12_C", "13_C"]
# suits = ["♠️", "♥️", "♦️", "♣️"]
suits = ["S", "H", "D", "C"]
hands = {}

#### FUNCTIONS ####

# Function to check the results of the hand
def check_hand(hand):
    num = [int(card[:-2]) for card in hand]
    suit = [card[-1] for card in hand]
    counts = []
    high_cards = [10, 11, 12, 13, 1]
    response = ""

    # Royal Flush - A, K, Q, J, 10, all with the same suit.
    if all(value in num for value in high_cards):
        if len(set(suit)) == 1: # Same Suit
            response = "Royal Flush"
    # Straight - Five cards in a sequence, but not of the same suit.        
        else:
            response = "Straight"
    # Flush	- Any five cards of the same suit, not in sequence.
    elif len(set(suit)) == 1: # Same Suit
        response = "Flush"
    
    # Straight Flush - Five cards in sequence, all with the same suit.       
    if sorted(num) == list(range(min(num), max(num)+1)):
         if len(set(suit)) == 1: # Same Suit
            response = "Straight Flush"
    # Straight - Five cards in a sequence, but not of the same suit.        
         else:
            response = "Straight"      
        


    for x in range(1, 14):
        counts.append(num.count(x))
    
    if 4 in counts:
        # Four of a Kind - Four cards of the same rank.
        response = "Four of a Kind"
    elif 3 in counts:
        if 2 in counts:
            # Full House - Three of a Kind with a Pair.
            response = "Full House"
        else:
            # Three of a Kind - Three cards of the same rank.
            response = "Three of a Kind"
    elif 2 in counts:
        two = counts.count(2)
        if two == 2:
            # Two Pair - Two different Pair.
            response = "Two Pair"
        else:
            # Pair - Two cards of the same rank.
            response = "One Pair"

    if response == "":
        # High Card - No other valid combination.
        if counts[0] == 1:
            high_card = "Ace"
        else:
            max_card = max(num)
            if max_card == 11:
                high_card = "Jack"
            elif max_card == 12:
                high_card = "Queen"
            elif max_card == 13:
                high_card = "King"
            else:
                high_card = str(max_card)
        
        response = "High Card is: " + high_card

    return response



# Function to deal 5 random cards and suits
def deal_cards():
    x = 5
    while len(cards) < 5:
        
        card = random.randint(1, 13)
        suit = random.randint(1, 4) - 1

        card = str(card) + "_" + suits[suit]

        if card not in cards:
            cards.append(card)
    
    cards.sort()
    return cards


#### INTERFACE ####

st.header("Poker | Pre-draw Odds")

with st.sidebar:
    wiki = """
    Royal flush <0.001%\n
    Straight flush (not including royal flush) <0.002%\n
    Four of a kind 0.02%\n
    Full house 0.14%\n
    Flush (excluding royal flush and straight flush) 0.20%\n
    Straight (excluding royal flush and straight flush) 0.39%\n
    Three of a kind 2.11%\n
    Two pair 4.75%\n
    One pair 42.30%\n
    No pair / High card 50.10%\n
    """

    st.write(wiki)

# Get the number of hands to deal from the user
num = st.number_input("How many hands do you want to deal? (Enter a number [1-100])", min_value=0, step=1)

results = []
# Loop num of times to generate a random hand, check results, and create the image path
if num >= 0 and num < 101:
    for h in range(0,num):
        hand = deal_cards()
        #hand = testing
        result = check_hand(hand)
        results.append(result)
        card = ["images/" + str(card) + ".png" for card in hand]
        hands[h] = card
        cards = []

    # Loop through number of hands in dictionary to create the images of 5 cards / hand
    for x in range(0,len(hands)):
        st.image(hands[x], width=100)
        st.info(results[x])
else:
    st.error("Error: Number must be between 1 and 100. Try again.")
