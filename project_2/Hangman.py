import random
from collections import Counter

def main():
    fruit_words_Array = ["Apple", "Mango", "Orange", "Banana","Kiwi", "Grapes", "Melon"]
    randomly_selected_fruit = random.choice(fruit_words_Array)
    print("I have chosen a word now is your time to guess it ", randomly_selected_fruit)
    for i in randomly_selected_fruit:
        print("_", end=" ")
    print()
    
    letter_guessed = ""    
    flag = True
    chances = len(randomly_selected_fruit) + 3
    correct = 0
    try: 
        while chances > 0 and flag == True:
            chances -= 1

            try:
                guess = str(input("Enter a word to guess: "))
            except:
                print("Please Enter Only Letter")
                continue

            if not guess.isalpha():
                print("Please Only Enter a word")
            elif len(guess) > 1:
                print("Please Provide One Letter at a time")
            elif guess in letter_guessed:
                print("You Already guessed that letter")
                continue
            
            if guess in randomly_selected_fruit:
                k = randomly_selected_fruit.count(guess)

                for _ in range(k):
                    letter_guessed += guess
            
            for char in randomly_selected_fruit:
                if char in letter_guessed and (Counter(letter_guessed)) != Counter(randomly_selected_fruit):
                    print(char, end=" ")
                    correct += 1
                elif Counter(letter_guessed) == Counter(randomly_selected_fruit):
                    flag = False
                    print("Congratulations Champ! You Won The Game.", end=" ")
                    print("The Game the word indeed was {}".format(randomly_selected_fruit))
                    break
                    break
                else:
                    print("_", end=" ")
        
        if chances <= 0 and Counter(letter_guessed) != Counter(randomly_selected_fruit):
            print()
            print("Uh Oh You Ran Out Of Chances... Lets Try Again!")
            print("The word was {}".format(randomly_selected_fruit))
    except KeyboardInterrupt:
        print()
        print("Bye Bye Try Again!")
        exit()
main()      