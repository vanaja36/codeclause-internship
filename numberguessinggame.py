import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_choosen):
    if level_choosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is to low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is two high")
        return attempts-1
    else:
        print(f"your guess is right... The answer was{answer}")


print("let me think of a number between 1 to 100")
answer=random.randint(1,100)
print(answer)
level=input("choose level of difficulty....Type 'easy' or 'hard' :")
attempts=set_difficulty(level)
guessed_number=0
while guessed_number!=answer:
    print(f"you have{attempts} attempts remaining to guess the number.")
    guessed_number=int(input("guess a number:"))
    attempts=check_answer(guessed_number,answer,attempts)
    if attempts==0:
        print("you are out of guesses...you loss!")
    else:
        print("Guess again")
