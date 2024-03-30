import random

answers = [
    "Undoubtedly", "It's a foregone conclusion", "Without any doubts", "Definitely yes", "You can be sure of this",
    "I think so", "Most likely", "Good prospects", "The signs say yes", "Yes",
    "Not clear yet, try again", "Ask later", "It's better not to tell", "Can't predict now",
    "Concentrate and ask again",
    "Do not even think", "My answer is no", "According to my data - no", "Prospects are not very good", "Very doubtful"
]


def greetings():
    """
    Shows the greetings and asks the user's name.
    """
    print('Hello World, I am a magic ball and I know the answer to any of your questions.')
    print('What is your name?')
    user_name = input()
    print(f'Hello, {user_name}!')


def replay():
    """
    Proposal to continue the game.
    """
    print('Wanna ask another question (Y/N)?')
    if input().lower() in ['y', 'Y', 'д', 'Д']:
        # print("Let's continue the game...\n")
        return True
    else:
        print('Thanks for playing. Come back if you have any questions!')
        return False


def game():
    """
    The main game loop.
    """
    while True:
        print('\nAsk your question')
        question = input()
        print(random.choice(answers))

        if replay():
            continue
        else:
            break


# Start the game
greetings()
game()
