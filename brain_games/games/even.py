import prompt
import random


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def ask_question():
    number = random.randint(1,100)
    print(f"Question: {number}")


def is_even(number):
    return number % 2 == 0


def get_answer():
    answer = prompt.string("Your answer: ")


def is_correct():
    if answer == 'yes' and is_even(number):
        return True
    elif answer == 'no' and not is_even(number):
        return True


def play_even():
    greet()
    print_rules()
    ask_question()
    get_answer()