reversed_symbols = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}


def split_to_divisions(num):
    digits = [int(d) for d in str(num)]
    increaser = 1
    i = len(digits) - 1
    while i >= 0:
        digits[i] *= increaser
        increaser *= 10
        i -= 1
    return digits


def arabian_to_roman(num):
    digits = split_to_divisions(num)
    result_list = []
    for digit in digits:
        if str(digit).startswith('4'):
            substracting_arabian = digit / 4
            prime_arabian = digit / 4 * 5
            substracting_roman = reversed_symbols[int(substracting_arabian)]
            result_list.append(substracting_roman)
            prime_roman = reversed_symbols[int(prime_arabian)]
            result_list.append(prime_roman)
        elif str(digit).startswith('9'):
            substracting_arabian = digit / 9
            prime_arabian = digit / 9 * 10
            substracting_roman = reversed_symbols[int(substracting_arabian)]
            result_list.append(substracting_roman)
            prime_roman = reversed_symbols[int(prime_arabian)]
            result_list.append(prime_roman)
        else:
            for value, symbol in reversed_symbols.items():
                while digit >= value:
                    result_list.append(symbol)
                    digit -= value
                    if digit == 0:
                        break
    return ''.join(result_list)

