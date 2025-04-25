import random
import sys
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
txt = ("BLACKJACK BITCH!!!")
x = txt.center(170)
print(x)
player=[]
computer=[]
player = [ random.choice(cards), random.choice(cards) ]
print(player)
computer = [ random.choice(cards), random.choice(cards) ]
print(computer)

def deal_player(player):
    choice = input("Hit or pass? ")
    choice=choice.upper()
    if (choice == 'HIT'):
        player.append(random.choice(cards))
        if sum(player) > 21:
            print(player)
            print("computer wins")
            sys.exit(0)
        elif sum(player) == 21:
            print(player)
            print("player wins")
            sys.exit(0)
        else:
            print(player)
            deal_player(player)
    else:
        print(player)
        return None

def deal_computer(computer):
    computer += [random.choice(cards), random.choice(cards)]
    if sum(computer) > 21:
        print(computer)
        print("player wins")
        sys.exit(0)
    elif sum(player) == 21:
        print(computer)
        print("player wins")
        sys.exit(0)
    else:
        print(computer)
        deal_computer(computer)
    if sum(computer)>=13:
        choice=random.choice([1,0])
        if(choice==1):
            computer += [random.choice(cards), random.choice(cards)]
            if sum(computer) > 21:
                print(computer)
                print("player wins")
                sys.exit(0)
            elif sum(player) == 21:
                print(computer)
                print("player wins")
                sys.exit(0)
            else:
                print(computer)
                deal_computer(computer)
        else:
            print(computer)
            return None
    else:
        print(computer)
        return None
print("player's turn")
deal_player(player)
print("computer's turn")
deal_computer(computer)

if sum(computer) == 21:
    print("computer wins")
else:
    if sum(player) > sum(computer):
        print("player wins")
    elif sum(computer) > sum(player):
        print("computer wins")


