import prompt


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def dialog(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def game(game_rule, question_and_right_answer):
    player_name = greeting()
    print(game_rule)
    quant_right_answer = 0
    CORRECT_ANSWER_COUNTER = 3
    while quant_right_answer < CORRECT_ANSWER_COUNTER:
        question, right_answer = question_and_right_answer()
        answer = dialog(question)
        if right_answer == answer:
            print("Correct!")
            quant_right_answer += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
    if quant_right_answer == 3:
        print(f"Congratulations, {player_name}!")
