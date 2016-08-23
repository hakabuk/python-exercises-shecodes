import random

LENGTH = 5


#Find a random five letter string in file; String
def random_str():
    line = ''
    while not (len(line) == LENGTH):
        line = random.choice(open('words.txt').readlines()).rstrip()
    return line


#Check valid guess: Checks if the length is LENGTH and that all characters are letters; Boolean
def check_valid(user_guess):
    return len(user_guess) == LENGTH and user_guess.isalpha()


#Checks Bulls and Cows; Returns list of 2 ints: [Bulls, Cows]
def check_guess(user_guess, to_guess):
    user_guess = user_guess.lower()
    score = [0,0]
    for i in range(LENGTH):
        if user_guess[i] in to_guess:
            if user_guess[i] == to_guess[i]:
                score[0] += 1
            else:
                score[1] += 1
    return score


def game():
    to_guess = random_str()
    print("The computer chose a random {} letters string".format(LENGTH))
    guess_flag = False

    while not (guess_flag):
        user_guess = str(input("Take a guess: What is the string the computer chose? "))
        if check_valid(user_guess):
            score = check_guess(user_guess, to_guess)
            if score[0] == LENGTH:
                print("You win! The computer string really is {}!".format(user_guess))
                guess_flag = True
            elif sum(score) == 0:
                print("No luck this time. You got 0 bulls and 0 cows. Try again.")
            else:
                print("Good job! You got {} bulls and {} cows. Keep going!".format(score[0], score[1]))
        else:
            print('Your guess is not valid')
    return


answer = "y"
while (answer == "y"):
    game()
    # lowercase and uppercase acceptable
    answer = input("Game Over\nPlay again? Y/N ").lower()