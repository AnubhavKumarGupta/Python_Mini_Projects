# simple_number_guess_game

from random import randint

# Initialize the range and generate a random target number
min_value, max_value = 1, 10
target_number: int = randint(min_value, max_value)
print(f'Try to guess the number between {min_value} and {max_value}.')

# Start the game loop
while True:
    # Get the player's guess
    try:
        player_guess: int = int(input('Your guess: '))
    except ValueError:
        print('Oops! Enter a valid integer.')
        continue

    # Compare the guess with the random number
    if player_guess > target_number:
        print('Too high! Try a smaller number.')
    elif player_guess < target_number:
        print('Too low! Try a larger number.')
    else:
        print('Congrats! You guessed correctly.')
        break
