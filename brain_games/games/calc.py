"""In this module, with 2 random numbers fron 1 to 50,
one of three arithmetic operations is randomly selected:
addition, subtraction or multiplication."""
import random


def operation_count():
    """Generate 2 random numbers.
    Randomly selects one operation from possible
    addition, subtraction or multiplication.
    Return the selected operation and
    the correct answer."""
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    choice_expression = random.randint(1, 3)
    if choice_expression == 1:
        result = first_num + second_num
        question = f"{first_num} + {second_num}"
        return question, str(result)
    elif choice_expression == 2:
        result = first_num - second_num
        question = f"{first_num} - {second_num}"
        return question, str(result)
    else:
        result = first_num * second_num
        question = f"{first_num} * {second_num}"
        return question, str(result)


game_rule = 'What is the result of the expression?'
