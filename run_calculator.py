import time
from calculate_roman import calculate_roman
from choose_output_style import choose_output_style


def run_calculator():
    print('Welcome to a simple calculator. Please read the instructions below.')
    time.sleep(1)
    print('Keep in mind that you have to enter two capitalized roman numbers separated by a sign.')
    time.sleep(1)
    input_roman = input('Enter your expression: ')
    math_result = calculate_roman(input_roman)
    time.sleep(1)
    print('Which output style to you prefer?')
    time.sleep(1)
    style = input('Please, choose one of the following options: roman or arabian and print it below: ')
    output_result = choose_output_style(math_result, style)
    time.sleep(1)
    print(f'The result is {output_result}.')
    time.sleep(1)
    print('Thank you for using this calculator!')
