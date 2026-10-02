import random

user_sc=0
comp_sc=0
options=["rock","paper","scissors"]
while True:
    user_ip=input("Enter :\n Rock \n Paper \n Scissors \n Q-Quit \n").lower()
    if(user_ip=="q"):
        break
    if user_ip not in options:
        continue

    num=random.randint(0,2)
    comp_ip=options[num]
    print("Computer picked :",comp_ip)

    if(user_ip=="rock" and comp_ip=="scissors"):
        print("Whoa !, You won ")
        user_sc+=1
        
    elif(user_ip=="paper" and comp_ip=="rock"):
        print("Whoa !, You won ")
        user_sc+=1
    elif(user_ip=="scissors" and comp_ip=="paper"):
        print("Whoa !, You won ")
        user_sc+=1
    elif((user_ip=="rock" and comp_ip=="rock") or (user_ip=="scissors" and comp_ip=="scissors") or (user_ip=="paper" and comp_ip=="paper")):
        print("Whoa !,it's a draw")
    
    else:
        print("Oops !,You lost ")
        comp_sc+=1
print("Scores :\n","You :",user_sc,"\nComp :",comp_sc)
print("Goodbye")
    