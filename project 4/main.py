username=input("Type your name: ")
print("Welcome", username, "to this adventure!")

answer=input("You're on a dirt road, it has come to an end and you can go left or right.Which way would you like to go: ").lower()
if answer =="left":
    answer=input("You came to a river, you can walk over it or swim across it.Which one do you wanna choose:").lower()
    if answer== "walk":
        print("You walked alot and died of thirst.You lose!")
    elif answer== "swim":
        print("You got eaten by an aligattor.You lose!")
    else:
        print("not a valid input.You lose!")
        
        
        
elif answer== "right":
    answer=input("You came to a bridge,,it looks wobbly,do you wanna go back or cross it?:").lower()
    if answer == "cross":
        print("Congrats you reached the town!You win!")
    elif answer == "go back":
        answer=input("You met a stranger on the way.Do you wanna talk with him?:").lower()
        if answer == "talk":
            print("He showed you the way out and you reached the town!You win!")
        else:
            print("You offended the stranger and he killed you!You lose!")
        
    
else:
    print("Not a valid input.You lose!")