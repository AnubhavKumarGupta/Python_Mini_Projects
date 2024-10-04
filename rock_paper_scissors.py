import random
import sys


class GameRPS:
    def __init__(self):
        print('Welcome to the Ultimate RPS Challenge!')

        # Mapping moves with emojis for display
        self.actions: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.choices: list[str] = list(self.actions.keys())

    def start_game(self):
        # User input for their move
        player_choice: str = input('Choose: Rock, Paper, or Scissors? >> ').strip().lower()

        # Option to quit the game
        if player_choice == 'quit':
            print('Goodbye! Thanks for playing!')
            sys.exit()

        # Validate user's choice, retry if invalid
        if player_choice not in self.choices:
            print('Invalid option. Try again...')
            return self.start_game()

        # AI randomly picks a move
        comp_choice: str = random.choice(self.choices)

        self.show_selections(player_choice, comp_choice)
        self.determine_winner(player_choice, comp_choice)

    def show_selections(self, player_choice: str, comp_choice: str):
        # Display player and AI choices
        print('====================')
        print(f'You chose: {self.actions[player_choice]}')
        print(f'Opponent chose: {self.actions[comp_choice]}')
        print('====================')

    def determine_winner(self, player_choice: str, comp_choice: str):
        # Game outcome determination logic
        if player_choice == comp_choice:
            print('It\'s a draw!')
        elif (player_choice == 'rock' and comp_choice == 'scissors') or \
             (player_choice == 'scissors' and comp_choice == 'paper') or \
             (player_choice == 'paper' and comp_choice == 'rock'):
            print('Congratulations, you are the winner!')
        else:
            print('You lost! The opponent wins.')

if __name__ == '__main__':
    game_instance = GameRPS()

    while True:
        game_instance.start_game()
