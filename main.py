import random

USER_WINS = 0
BOT_WINS = 0


def intro():
    """Display the game intro text"""
    print("------------------------------")
    print("Welcome to Rock-Paper-Scissors")
    print("------------------------------")
    print("----------(Q to Quit)---------")
    print()
    print("Choose your weapon!")


def play():
    """Ask user for input and display result"""
    global USER_WINS, BOT_WINS

    player_input = input("Rock/Paper/Scissors: ").lower()
    if player_input == 'q':
        print("Thanks for playing")
        exit()

    bot_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"The bot played {bot_choice}")

    if player_input == bot_choice:
        print("Its a tie!")

    if has_won(player_input, bot_choice):
        USER_WINS += 1
        print("You WON!")
    else:
        BOT_WINS += 1
        print("You LOST!")

    print()


def has_won(user, computer):
    """Determine if the user has won"""
    # R > S, S > P, P > R
    if ((user == 'rock' and computer == 'scissors')
            or (user == 'scissors' and computer == 'paper')
            or (user == 'paper' and computer == 'rock')):
        return True


def game_loop():
    """Loop game mechanism and display win counter"""
    while True:
        play()

        print(f"User Wins: {USER_WINS}")
        print(f"Computer Wins: {BOT_WINS}")
        print("------------------------------")
        print()


intro()
game_loop()
