"""all_dvizh module. Contains main logic for all brain games."""


import prompt

from brain_games.games.do_calc import do_calc
from brain_games.games.do_even import do_even
from brain_games.games.do_gcd import do_gcd
from brain_games.games.do_prime import do_prime
from brain_games.games.do_progr import do_progr

NUMBER_OF_CYCLES = 3

txt01 = 'Welcome to the Brain Games!'
txt02 = 'May I have your name? '
txt03 = 'Hello, {0}!'
txt04 = 'Answer "yes" if the number is even, otherwise answer "no".'
txt05 = 'Answer "yes" if given number is prime, otherwise answer "no".'
txt07 = 'What is the result of the expression?'
txt08 = 'Find the greatest common divisor of given numbers.'
txt09 = 'What number is missing in the progression?'
txt10 = 'Question: {0} {1} {2}'
txt11 = 'Question: {0} {1}'
txt12 = 'Question: {0}'
txt13 = 'Your answer: '
txt14 = 'Correct!'
txt15 = 'Congratulations, {0}!'
txt16 = "'{0}' is wrong answer ;(. "
txt17 = "Correct answer was '{0}'."
txt18 = "Let's try again, {0}!"



var_answers = {
        do_even: [txt04, txt12, prompt.string],
        do_calc: [txt07, txt10, prompt.integer],
        do_gcd: [txt08, txt11, prompt.integer],
        do_progr: [txt09, txt12, prompt.integer],
        do_prime: [txt05, txt12, prompt.string]
    }

# flake8: noqa: C901
def central_function(scenario):
    """Do the main logic. In argument scenario - name of function to do."""
    print(txt01)
    user_name = prompt.string(txt02)
    print(txt03.format(user_name))

   
    
    print(var_answers[scenario][0])
    quant = 0
    while quant < NUMBER_OF_CYCLES:
        
        operat_question, correct_result = scenario()

        
        print(operat_question)
        
        user_result = (var_answers[scenario][2])(txt13)
        
       

        if user_result != correct_result:
            print(txt16.format(user_result), end='')
            print(txt17.format(correct_result))
            print(txt18.format(user_name))
            break

        print(txt14)
        quant = quant + 1
    if quant == NUMBER_OF_CYCLES:
        print(txt15.format(user_name))
