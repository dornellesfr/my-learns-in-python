def guess_secret():
    SECRET = "potato"
    bet = len(SECRET) * "*"
    counter = 0
    print("-------GUESS GAMESHOW-------")

    while True:
        print("~" * 60)
        print(f"Tries: {counter}")
        print(f"Word:\n{bet}")
        try:
            letter_to_guess = input("Type a letter: ").lower()
            different_1 = len(letter_to_guess) > 1 or 1 > len(letter_to_guess)
            if different_1:
                raise ValueError()
        except ValueError:
            print("You type must be a unique letter, type again...")
            continue

        if letter_to_guess in SECRET:
            print("You guessed right!")

            list_bet = [letter for letter in bet]
            list_secret = [letter for letter in SECRET]

            for position, letter in enumerate(list_secret):
                if letter == letter_to_guess:
                    list_bet[position] = letter
            bet = ''.join(list_bet)
            print(bet)
        else:
            print("Guess not right!")

        if bet == SECRET:
            print('Congrats, you guessed the word!')
            break

        counter += 1


guess_secret()
