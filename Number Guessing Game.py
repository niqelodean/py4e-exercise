secret_num = 7
attempts_left = 3
guessed_correctly = False

while attempts_left > 0:
    usernumber = int(input("Guess a number: "))
    
    if usernumber == secret_num:
        print("Congrats!")
        guessed_correctly = True
        break
    elif usernumber < secret_num:
        print("Go higher")
    else:
        print("Go lower")
        
    attempts_left -= 1
    print(f"Attempts remaining: {attempts_left}\n")

if not guessed_correctly: #if guessed_correctly still False this code will run
    print(f"You lose! The secret number was {secret_num}")
