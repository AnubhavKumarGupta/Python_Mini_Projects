from random import choice


def start_game():
    secret_word: str = choice(['apple', 'secret', 'banana'])

    # Welcome message for the player
    player_name: str = input('Enter your name: >> ')
    print(f'Hello {player_name}, welcome to the guessing game!')

    # Game setup
    used_letters: str = ''  # Track all guessed letters
    remaining_attempts: int = 3  # Number of attempts allowed

    # Game loop
    while remaining_attempts > 0:
        missing_letters: int = 0

        print('Word: ', end='')
        for letter in secret_word:
            if letter in used_letters:
                print(letter, end='')
            else:
                print('_', end='')
                missing_letters += 1

        print()  # New line for better output formatting

        # Check if the player has guessed the word
        if missing_letters == 0:
            print('Congratulations, you guessed the word!')
            break

        # Player's guess input
        player_guess: str = input('Guess a letter: ')

        # Check if the letter was already guessed
        if player_guess in used_letters:
            print(f'You have already guessed "{player_guess}". Try a new letter!')
            continue

        # Add guessed letter to the list of used letters
        used_letters += player_guess

        # Check if the guess is not in the word
        if player_guess not in secret_word:
            remaining_attempts -= 1
            print(f'Wrong guess... You have {remaining_attempts} attempts left.')

            # If no attempts left, player loses
            if remaining_attempts == 0:
                print('You have no attempts left. Game over!')
                break


if __name__ == '__main__':
    start_game()
