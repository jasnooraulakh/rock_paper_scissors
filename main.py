import random


def play():

    player_input = input("Choose your weapon: Rock/Paper/Scissors ").lower()
    bot_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"The bot played {bot_choice}")

    if player_input == bot_choice:
        print("Its a tie!")

    if has_won(player_input, bot_choice):
        print("You won!")
    else:
        print("You lost!")


def has_won(user, computer):

    # R > S, S > P, P > R
    if ((user == 'rock' and computer == 'scissors')
            or (user == 'scissors' and computer == 'paper')
            or (user == 'paper' and computer == 'rock')):

        return True


play()
