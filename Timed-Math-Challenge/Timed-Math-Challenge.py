import random
import time

operators=["+","-","*"]
min_operand=3
max_operand=12
Total_Problems=10

def Generate_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)

    expr=str(left)+ operator+ str(right)
    ans=eval(expr)
    return expr,ans

wrong=0
print("------------------- WELCOME TO THE ULTIMATE MATH CHALLENGE ! TIME TO TEST YOUR MATH REFLEXES ----------------------")
input("Press Enter to start !")
start_time = time.time()
for i in range(Total_Problems):
    expr,ans=Generate_problem()
    while True:
        user=input("Problem # " + str(i+1) + ": " + expr +" = ")
        if user==str(ans):
            break
        wrong+=1

end_time = time.time()
total_time= round(end_time - start_time,2)
print("------------------------------------------------------------------------------------------------------------------")
print("Great Job ! Got ",Total_Problems-wrong , "correct out of",Total_Problems)
print("You finished in ",total_time,"seconds !")
