#Number Guessing Game

'''Rules:

Secret number = 25
User gets 5 chances
Show Higher/Lower hints'''

secret_number = 25
attempts = 5
print("----Guessing Game -----")
print("You will only got 5 chances to guess it right!")

while attempts > 0:
    guess = int(input("Your Guess ?: "))
    
    if guess == secret_number:
        print("Whoaa!!!, you guessed it.")
        break
    else:
        attempts-=1
        if guess > secret_number:
            print("guess lower!")
            print(f"attempts remaining {attempts}")
        else:
            print("guess higher!")
            print(f"attempts remaining {attempts}")


