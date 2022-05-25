import json
import random
import datetime

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

new_list = sorted(score_list, key=lambda item: item['attempts'])[:3]

for score_dict in new_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

name = input("Enter your name: ")

wrong_guesses = {name: []}

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()),
                           "secret": secret})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        print(wrong_guesses[name])
        break

    elif guess > secret:
        wrong_guesses[name].append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        wrong_guesses[name].append(guess)
        print("Your guess is not correct... try something bigger")