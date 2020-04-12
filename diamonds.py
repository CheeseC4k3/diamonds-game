#!/usr/bin/python3
import random

#idea + rules



# general functions
def nl():
    print("\n")

#set up classes for players
class player:

    playerCount = 0

    def __init__(self, name, risk, diamonds, state):
        self.name = name
        self.risk = risk
        self.diamonds = diamonds
        self.state = state
        player.playerCount += 1

    def displayCountP(self):
        print(playerCount)

class card:

    cardCount = 0

    def __init__(self, name, type, value, number):
        self.name = name
        self.type = type
        self.value = value
        self.number = number
        player.playerCount += 1*int(number)

        def displayCountC(self):
            print(cardCount)

#Initial card stack

oneD = card("One Diamond", "Treasure", 1, 1)
twoD = card("Two Diamonds", "Treasure", 2, 1)
threeD = card("Three Diamonds", "Treasure", 3, 1)
fourD = card("Four Diamonds", "Treasure", 4, 1)
fiveD = card("Five Diamonds", "Treasure", 5, 1)
sixD = card("Six Diamonds", "Treasure", 6, 1)
sevenD = card("Seven Diamonds", "Treasure", 7, 1)
eightD = card("Eight Diamonds", "Treasure", 8, 1)
nineD = card("Nine Diamonds", "Treasure", 9, 1)
tenD = card("Ten Diamonds", "Treasure", 10, 1)
elevenD = card("Eleven Diamonds", "Treasure", 11, 1)
twelveD = card("Twelve Diamonds", "Treasure", 12, 1)
thirteenD = card("Thirteen Diamonds", "Treasure", 13, 1)
fourteenD = card("Fourteen Diamonds", "Treasure", 14, 1)
fifteenD = card("Fifteen Diamonds", "Treasure", 15, 1)
snake = card("Snake", "hazard", 0, 3)
witch = card("Witch", "hazard", 0, 3)
rockfall = card("Rockfall", "hazard", 0, 3)
spiders = card("Spiders", "hazard", 0, 3)
fire = card("Fire", "hazard", 0, 3)
llama = card("Golden Llama", "artifact", 5, 1)
statue = card("Statue of the Sun God", "artifact", 5, 1)
knive = card("Ceremonial Knife", "artifact", 5, 1)
cup = card("Golden Cup", "artifact", 5, 1)
map = card("Treasure Map", "artifact", 5, 1)

allcards = [oneD, twoD, threeD, fourD, fiveD, sixD, sevenD, eightD, nineD, tenD, elevenD, twelveD, thirteenD, fourteenD, fifteenD, snake, witch, rockfall,
spiders, fire, llama, statue, knive, cup, map]
#initiate NPCs

npc1 = player("max", 1, 0, "start")
npc2 = player("hannah", 2, 0, "start")
npc3 = player("vic", 4, 0, "start")

#Welcome Message
print("Welcome to Aztec Gold")
nl()

#Initiate human player
name = input("Please enter your name! ")

player1 = player(name, 0, 0, "start")
nl()
print("Welcome, " + player1.name +", to the ruins of Tenochtitlan!")
print("You are on an expedition with three compagnions. Your goal is to collect as many diamonds as you can!")
print("But behold! Deadly hazards await you..")

# create first cardstack

deck = []

for card in allcards:
    for i in range(card.number):
        deck.append(card)

path = []

# draw random cards and add it to the path until one appears twice or player goes to camp
while True:

    player1.state = "make_decision"
    randomcard = random.choice(deck)
    print("A card was drawn: " + randomcard.name)
    #for i in path:
    path.append(randomcard)
    deck.remove(randomcard)
    if len(path) == len(set(path)):
        print("Look back on the path and see: ")
        [print(i.name) for i in path]
        input("do you want to continue?")
        while player1.state != "t" and player1.state != "c":
            player1.state = input("type 'c' to leave for the camp or 't' to stay in the temple")
    else:
        print("Oh no, " + randomcard.name + " has appeared twice! You lose")
        input("press 'enter' to exit")
        break
    if player1.state == "c":
        for card in path:
            player1.diamonds += card.value
        print("You return to camp and collect " + str(player1.diamonds) + " diamonds")
        input("press 'enter' to exit")
        break
