from roman_to_arabian import roman_to_arabian


def calculate_roman(expression):
    listed_expression = expression.split(' ')
    first_number, expression_sign, second_number = listed_expression
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
