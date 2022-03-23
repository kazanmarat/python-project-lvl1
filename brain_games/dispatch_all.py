"""all_dvizh module. Contains main logic for all brain games."""


import prompt

#from brain_games.games.do_calc import do_calc
#from brain_games.games.do_even import do_even
#from brain_games.games.do_gcd import do_gcd
#from brain_games.games.do_prime import do_prime
#from brain_games.games.do_progr import do_progr

#import brain_games.games.do_even

#NUMBER_OF_CYCLES = 3

WELCOME_TEXT = 'Welcome to the Brain Games!'
ASK_NAME = 'May I have your name? '
GREET_TXT = 'Hello, {0}!'
txt14 = 'Correct!'
txt15 = 'Congratulations, {0}!'
txt16 = "'{0}' is wrong answer ;(. "
txt17 = "Correct answer was '{0}'."
txt18 = "Let's try again, {0}!"

def dispatch_all(FUNC_TXT, operat_question, correct_result):
    print(WELCOME_TEXT)
    user_name = input(ASK_NAME)
    print(GREET_TXT.format(user_name))
    
    
    print(FUNC_TXT)
    quant = 0
    while quant < 3:
        
        print('Question:', operat_question)
        user_result = input('Your answer: ')
        if str(user_result) != str(correct_result):
            print(txt16.format(user_result), end='')
            print(txt17.format(correct_result))
            print(txt18.format(user_name))
            break
        

        print(txt14)
        quant = quant + 1
    if quant == 3:
        print(txt15.format(user_name))



#txt10 = 'Question: {0} {1} {2}'
#txt11 = 'Question: {0} {1}'
#txt12 = 'Question: {0}'
#txt13 = 'Your answer: '
#txt14 = 'Correct!'
#txt15 = 'Congratulations, {0}!'
#txt16 = "'{0}' is wrong answer ;(. "
#txt17 = "Correct answer was '{0}'."
#txt18 = "Let's try again, {0}!"



#var_answers = {
#        do_even: [txt12],
#        do_calc: [txt10],
#        do_gcd: [txt11],
#        do_progr: [txt12],
#        do_prime: [txt12]
#    }

# flake8: noqa: C901
#def dispatch_all(scenario):
#    """Do the main logic. In argument scenario - name of function to do."""
#    print(WELCOME_TEXT)
#    user_name = prompt.string(ASK_NAME)
#    print(GREET_TXT.format(user_name))

    
    
#    print('var_answers[scenario][0]')
#    quant = 0
#    while quant < NUMBER_OF_CYCLES:
        
#        FUNC_TXT, operat_question, correct_result = scenario()

        
#        print(operat_question)
        
#        user_result = input(txt13)
        
       

#        if str(user_result) != str(correct_result):
#            print(txt16.format(user_result), end='')
#            print(txt17.format(correct_result))
#            print(txt18.format(user_name))
#            break

#        print(txt14)
#        quant = quant + 1
#    if quant == NUMBER_OF_CYCLES:
#        print(txt15.format(user_name))
