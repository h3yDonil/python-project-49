import prompt
import random

number_of_questions = 3

def play_even():
    name = greet()
    print_rules()
    questions = generate_questions(number_of_questions)
    game_loop(questions, name)


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def generate_questions(number_of_questions):
    questions = []
    for _ in range(number_of_questions):
        number = random.randint(1, 100)
        if is_even(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        item = [number, correct_answer]
        questions.append(item)

    return questions


def game_loop(questions, player_name):
    victory_count = 0
    for question, correct_answer in questions:
        print(f"Question: {question}")
        player_answer = prompt.string("Your answer: ")
        if player_answer == correct_answer:
            print('Correct')
            victory_count += 1
            if victory_count == 3:
                print(f'Congratulations, {player_name}!')
        else:
            print(f"'{player_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            exit(0)




