print("Welcome to the shit app/game")

playing = input("Do you want to play? ")
count = 0

if playing.lower() != "yes":
    quit()

print("Let's begin!")

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
