
import random

arr=[]
secret=random.randint(1,20)
while True:
    print("Welcome to SecretGuess:")
   
    user_input=input("Guess the secret number:").strip().lower()
    if user_input in ["quite","q"]:
        print("Game over, Thank you for playing")
        break
    
    try:
        guess=int(user_input)
    except ValueError:
       print("Please enter a number")
       continue
    arr.append(guess)
    if guess<secret:
        print("Too low than the secret")
    elif guess>secret:
        print("Too higher than the secret")
    else:
        print(f"CORRECT the secret number if {guess}:you have guessed {len(arr)} times")
        break
    
   