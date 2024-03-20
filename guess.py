import random
import math

lower_bond=int(input("Enter the lower range : "))
upper_bond=int(input("Enter the upper range : "))

x=random.randint(lower_bond,upper_bond)
chance=round(math.log(upper_bond - lower_bond + 1, 2))
print(f"You have {chance} chances to find the number")
count=0
while(count<=chance):
    count+=1
    guess=int(input("Enter the number : "))

    if guess==x:
        print(f"Congrates the number is right you guess in {count} chances ")
    
    elif guess>x:
        print(f"You guess too high. Remaing chances : {chance-count}")
    elif guess<x:
        print(f"you guess too small. Remaing chances : {chance-count}")

if count>=chance:
    print(f"The number is : {x}")