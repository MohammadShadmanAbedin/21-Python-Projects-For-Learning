print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score=0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else: print("Oh no! Incorrect")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else: print("Oh no! Incorrect")

answer = input("What does psu stand for? ").lower()
if answer == "power supply unit":
    print('Correct!')
    score += 1
else: print("Oh no! Incorrect")

answer = input("What does gpu stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else: print("Oh no! Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")
