import random

user_number = input("Enter a number: ")
guess = 0
if user_number.isdigit():
    user_number = int(user_number)
    
    if user_number <= 0 :
        print("Enter number larger than 0 next time!")
        quit()
         
else:
    print("Enter a number next time!")
    quit()
    
random_number = random.randint(0, user_number)


while True:
    guess += 1
    guess_number = input("Make a guess: ")
    if guess_number.isdigit():
     guess_number = int(guess_number)
    
    else:
     print("Enter a number next time!")
     quit()
     continue

    if guess_number == random_number:
        print("You've guessed the correct number!")
        break
    elif guess_number > random_number:
        print("You got it wrong!")
        print("you were above the number! Try guessing a lower number.")
    else: 
        print("you were below the number! Try guessing the higher number.")

print("You got it in", guess, "Guesses.")
   
 
