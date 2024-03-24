from arabian_to_roman import arabian_to_roman


def choose_output_style(math_result, style):
    output = None
    if style == 'arabian':
        output = math_result
    if style == 'roman':
        output = arabian_to_roman(math_result)
    return output
