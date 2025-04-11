import prompt
import random


def play_even():
    game_loop()

def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def print_question():
    random_number = random.randint(1,100)
    print(f'Question: {random_number}')


def get_answer():
    name = prompt.string('Your answer: ')


def is_even(number):
    return number % 2 == 0


def check_answer(answer):
    correct_answers = ['yes', 'no']
    if answer not in correct_answers:
        print(f"'{answer}' is wrong answer ;(.")
    elif answer == 'yes' and is_even:
        print('Correct!')
        win_count += 1





