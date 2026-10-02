import random

def roll():
    roll=random.randint(1,6)
    return roll






print("                                          WELCOME ")
play=input("Ready to play PIG ? ").lower()
if(play !="yes"):
    quit()
else:
    print ("**************************     Rules to play PIG      ****************************")
    print("Roll the die as many times as you want on your turn.\nIf you roll a 1, you lose all points for that turn.\n ")
    print("Let's Begin ! ")


while True:
    players=input("Enter no. of players (2-4) : ")
    if(players.isdigit()):
        players=int(players)
        if(2<=players<=4):
            break
        else:
            print("Must be between 2-4 .")
            continue
    else:
        print("Enter correctly")
        continue

max_score=50
players_score=[0 for _ in range(players)]
while max(players_score)< max_score:
    for i in range(players):
        print("Player",i+1,"turn has started !")
        
        current_score=0
        while True:
            turn=input("Would you like to roll ?(y/n) ").lower()
            if(turn !="y"):
                break
            value=roll()
            if(value==1):
                print("Oop's you rolled a one , turn done !")
                current_score=0
                break
            else: 
                current_score+=value
                print("You rolled a",value)
               
            print("Player",i+1,"score is",current_score)
        players_score[i]+=current_score
        print("Your total score is",players_score[i])

win=max(players_score)
print("Hurrayy ! , Player number ",players_score.index(win)+1,"has won with points",win)