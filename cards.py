


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

if value = 1:
    value = 10
elif value.isdigit():