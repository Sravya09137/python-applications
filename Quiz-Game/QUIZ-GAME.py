print("Welcome to the quiz")

play=input("Do you want to play ? ")
print(play)
play=play.lower()
if play!="yes" :
    quit()

else:
    print("Let's start !")

score=0
print("Choose your quiz category :\n  1.General Knowledge \n  2.Science Facts \n 3.Movies ans TV Shows")
option=int(input("Enter any number :"))

if(option==1):
    print("Great choice , General Knowledge \n")
    #1
    ans=input("What is the largest ocean in the world ? ")
    ans.lower()
    if(ans=="pacific ocean"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    #2
    ans=input("Who was the first person to step on the Moon ? ")
    ans.lower()
    if(ans=="neil armstrong"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")

    #3
    ans=input("What is the currency of Japan? ")
    ans.lower()
    if(ans=="yen"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("You got",score,"\nGreat !")
elif(option==2):
    score=0
    print("Great choice , Science Facts \n")
    #1
    ans=input("What is the center of an atom called ? ")
    ans.lower()
    if(ans=="nucleus"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    #2
    ans=input("Which organ pumps blood throughout the human body ? ")
    ans.lower()
    if(ans=="heart"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")

    #3
    ans=input("Which planet is closest to the Sun? ")
    ans.lower()
    if(ans=="mercury"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("You got",score,"\nGreat !")
elif(option==3):
    print("Great choice , Movies and TV Shows \n")
    #1
    ans=input(" In which TV show do six friends hang out at Central Perk Café ? ")
    ans.lower()
    if(ans=="friends"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    #2
    ans=input("Which Marvel movie introduced Iron Man ? ")
    ans.lower()
    if(ans=="iron man"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")

    #3
    ans=input("In the movie The Lion King, what is the name of Simba’s father? ")
    ans.lower()
    if(ans=="mufasa"):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("You got",score,"\nGreat !")
else:
    print("Wrong choice entered !")


