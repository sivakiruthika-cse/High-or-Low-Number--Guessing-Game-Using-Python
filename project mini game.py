import random

print("High or Low Game")

while True:
    first = random.randint(1, 20)
    print("First number is:", first)

    second = int(input("Enter the second number (1-20): "))

    choice = input("Is the second number high or low? ")
    print("\n")

    if (choice == "high" and second > first) or \
       (choice == "low" and second < first):
       
        print("You win the game 🤩, Great job!! 😎")
        print("\n")
        print("Next Round Starts...\n")

    else:
        print("You lose the game 😔, Well played!! 😊")
        print("\n")
        print("Game Over")
        break
