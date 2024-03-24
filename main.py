import time

from roman_to_arabian import roman_to_arabian
from arabian_to_roman import arabian_to_roman


def calculate_roman():
    print('Welcome to a simple calculator. Please read the instructions below.')
    time.sleep(1)
    print('Keep in mind that you have to enter two capitalized roman numbers separated by a sign')
    time.sleep(1)
    input_roman = input('Enter your expression: ')
    listed_expression = input_roman.split(' ')
    first_number = listed_expression[0]
    second_number = listed_expression[2]
    expression_sign = listed_expression[1]
    calculated_result = None
    match expression_sign:
        case '+':
            calculated_result = roman_to_arabian(first_number) + roman_to_arabian(second_number)
        case '-':
            calculated_result = roman_to_arabian(first_number) - roman_to_arabian(second_number)
        case '*':
            calculated_result = roman_to_arabian(first_number) * roman_to_arabian(second_number)
        case '/':
            calculated_result = round(roman_to_arabian(first_number) / roman_to_arabian(second_number))
        case _:
            calculated_result = 'Invalid sign, please try again.'
    return calculated_result


math_result = calculate_roman()


def choose_output_style():
    time.sleep(1)
    print('Which output style to you prefer?')
    time.sleep(1)
    style = input('Please, choose one of the following options: roman or arabian and print it below: ')
    output = None
    if style == 'arabian':
        output = math_result
    if style == 'roman':
        output = arabian_to_roman(math_result)
    return output


output_result = choose_output_style()
time.sleep(1)
print(f'The result is {output_result}')