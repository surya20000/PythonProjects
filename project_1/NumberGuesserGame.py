import random

def main():
    print("Welcome user to this platform of number guessing game enter a range of numbers eg. 1 50 here 1 is the first and 50 is another")
    user_entered_range = list(map(int,input().split()))
    [lower_range, higher_range] = user_entered_range
    computer_generated_integer = random.randint(lower_range, higher_range)
    print("I have guessed an Integer now you have to guess that number between that range only. Remember You have Three Chances Only", computer_generated_integer)
    for i in range(3):
        user_guessed_number = int(input(f"Attempt {i + 1}: Enter your guess: "))
        
        if user_guessed_number == computer_generated_integer:
            print("Congratulations! You guessed the number correctly! It was", computer_generated_integer)
            break 
        elif user_guessed_number < lower_range or user_guessed_number > higher_range:
            print(f"Your guess is out of range! Please guess a number between {lower_range} and {higher_range}.")
        elif user_guessed_number > computer_generated_integer:
            print("Try Again! You guessed too high!")
        else:
            print("Try Again! You guessed too low!")
    else:
        print("Sorry, you've used all your chances. The correct number was", computer_generated_integer)
    
main()
