import random 

low = 1
high = 100

guesses = 0
number = random.randint(low, high) 

while True: 
    guess = int(input(f"Enter a number between {low} through {high}: "))
    guesses += 1
    
    if guess < number:
        print("Too low, Please try again: ")
    elif guess > number:
        print("Too high, Please try again: ")
    else:
        print(f"{guess} is correct!")
        print(f"This round took you {guesses} guesses. ") 

