import random

play=input("Want to play ? : Yes or No ").lower()
if(play!="yes"):
    quit()

else:
    print("Guess the number !")
    num=input("Enter a range upto which you want to guess :")
    if(num.isdigit()):
        num=int(num)
        ran=random.randint(1,num)
        guesses=0

        while True:
            guesses+=1
            guess=input("Make a guess:") 
            if(guess.isdigit()):
                guess=int(guess)
                if(guess<ran):
                    print("Enter a higher number")
                elif(guess>ran):
                    print("Enter a smaller number")
                elif(guess==ran):
                    print("Yay,you got it correct !",ran)
                    print("In ",guesses,"guesses")
                    break
                
                 
            else:
               print("Please give a valid number !")

    else:
        print("Please give a valid range !")