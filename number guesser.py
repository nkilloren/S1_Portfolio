#Noah Killoren

#11/11
import random
answer = random.randint(1,10)
two_guess = "dog" #This is just to set the variables
final_guess = "cat"
print("Welcome to the random number game. Please follow the instructions to play.")
def game():
    global final_guess
    global two_guess
    guess= int(input("Guess a number 1-10"))#From here to line 20 is the feedback from your first guess, where is is either too high, low, or spot on
    if guess == answer:
        print("Congrats, you guessed correctly, the number was "+str(answer))
    if guess > answer:
        print("Sorry, your answer was too high, but try again")
        two_guess=int(input("Guess a different number 1-10"))
    if guess < answer:
        print("Sorry, your answer was too low, but try again")
        two_guess=int(input("Guess a different number 1-10"))
    if two_guess == answer:#This is the feedback from your second guess, which pairs feedback from the first and seconrd guess
        print("You got it this time! The number was " + str(answer) +".")
    if two_guess == "dog":
        print("Please play again!")
    if guess> answer and two_guess>answer:
        print("Your guess is still two high, try again.")
        final_guess=int(input("Guess a different number 1-10, based on your first two guesses"))
    if guess> answer and two_guess <answer:
        print("Now your guess was too low, try again.")
        final_guess=int(input("Guess a different number 1-10, based on your first two guesses"))
    if guess< answer and two_guess <answer:
        print("Your guess is still too low, try again.")
        final_guess=int(input("Guess a different number 1-10, based on your first two guesses"))
    if guess <answer and two_guess>answer:
        print("Now your guess is too high, try again.")
        final_guess=int(input("Guess a different number 1-10, based on your first two guesses"))
    if final_guess == answer:#Finally we are at the last guess, where you either get it right or wrong
        print("Congrats, you finally got it! Play again if you would like")
    if final_guess == "cat":
        print("Please play again!")
    else:# This shows the user the correct number
        print("Sorry you couldn't get it. The answer was " + str(answer) + ". Play again if you would like")
game()

