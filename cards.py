
#Cards
A = "Ace"
K = "King"
Q = "Queen"
J = "Jack"

D = "Diamonds"
H = "Hearts"
S = "Spades"
C = "Clubs"


cardNote = input("Enter the card notation: ").upper()
value = cardNote[0]
suit = cardNote[-1]

# determine value of the cards
if value == "1":
    value = "10"
elif value == "A":
    value = A
elif value == "K":
    value = K
elif value == "Q":
    value = Q
elif value == "J":
    value = J

# determine the suit
if suit == "D":
    suit = D
elif suit == "H":
    suit = H
elif suit == "S":
    suit = S
elif suit == "C":
    suit = C

# Output
print(f"{value} of {suit}")