import random

answers = [
    "Undoubtedly", "It's a foregone conclusion", "Without any doubts", "Definitely yes", "You can be sure of this",
    "I think so", "Most likely", "Good prospects", "The signs say yes", "Yes",
    "Not clear yet, try again", "Ask later", "It's better not to tell", "Can't predict now",
    "Concentrate and ask again",
    "Do not even think", "My answer is no", "According to my data - no", "Prospects are not very good", "Very doubtful"
]


def greetings():
    print('Hello World, I am a magic ball and I know the answer to any of your questions.')
    print('What is your name?')
    user_name = input()
    print(f'Hello, {user_name}!')


greetings()
