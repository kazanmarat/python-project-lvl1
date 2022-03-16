"""Module do_calc. Do main calculations and return results to the main."""


from random import choice

def do_calc(numb1, numb2):
    """Do calculates brain_calc.
    Parameters: - numb1 and numb2 are random numbers.
    Returns: result of mathem. operation.
    """
    text01 = 'Question: {0} {1} {2}'
    text02 = 'Your answer: '
    my_choice = choice(['add', 'subtr', 'multipl'])

    if my_choice == 'add':
        print(text01.format(numb1, '+', numb2))
        answer = int(input(text02))
        result_add = numb1 + numb2
        return (answer, result_add)
    if my_choice == 'subtr':
        print(text01.format(numb1, '-', numb2))
        answer = int(input(text02))
        result_subtr = numb1 - numb2
        return (answer, result_subtr)
    if my_choice == 'multipl':
        print(text01.format(numb1, '*', numb2))
        answer = int(input(text02))
        result_multipl = numb1 * numb2
        return (answer, result_multipl)
