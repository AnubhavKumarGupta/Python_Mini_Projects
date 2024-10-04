import random


def dice_roll(count: int = 2) -> list[int]:
    if count <= 0:
        raise ValueError("Number of dice should be positive.")

    outcomes: list[int] = []
    for _ in range(count):
        roll_value: int = random.randint(1, 6)
        outcomes.append(roll_value)

    return outcomes


def play():
    while True:
        try:
            user_choice: str = input('Enter the number of dice to roll or type "exit" to quit: ')

            # Exit condition
            if user_choice.lower() == 'exit':
                print('Exiting the game. Thanks for participating!')
                break

            # Convert input to integer and roll dice
            print(*dice_roll(int(user_choice)), sep=', ')
        except ValueError:
            print('Invalid input, please provide a valid number.')


if __name__ == '__main__':
    play()
