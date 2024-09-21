import random

good_number = random.choice(range(1, 101))
levels = {'hard': 5, 'easy': 10}

chose_level = input("choose a difficulty 'easy' or 'hard' ? :  ")
while chose_level not in levels:
    chose_level = input("please choose a difficulty between 'easy' and 'hard' ? :  ")

rounds = 0
rounds_past = 0
user_got_it = False

for level in levels:
    if chose_level == level:
        rounds = levels[level]

print(f"you have {rounds} attempts to find the number ")
while rounds > 0:
    guess_number: int = int(input("make a guess: "))
    if guess_number == good_number:
        user_got_it = True
        break
    elif guess_number > good_number:
        print("too high...")
    else:
        print("too low...")
    rounds = rounds - 1
    rounds_past += 1
    if rounds > 0:
        print("guess again")
        print(f"you have {rounds} attempts remeaning to guess the number ")

if user_got_it:
    print(f"you got it {good_number} in {rounds_past} rounds")
else:
    print(f"you lose the good number was: {good_number}")