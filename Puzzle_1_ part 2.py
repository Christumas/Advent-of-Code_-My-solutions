import re

numbers = [str(i) for i in range(0, 10)]
num_letters = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9',
               'ten': '10'
               }

possibilities = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
             '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('input.txt', 'r') as file:
    lines = file.readlines()


def updated_calval(list):
    regex = re.compile('|'.join(possibilities))
    cal_vals = []

    for i in list:
        first_digit = ''
        last_digit = ''
        matches = re.findall(regex, i)
        if matches[0] in num_letters:
            first_digit += num_letters[matches[0]]
        elif matches[0] in numbers:
            first_digit += matches[0]
        if matches[-1] in num_letters:
            last_digit += num_letters[matches[-1]]
        elif matches[-1] in numbers:
            last_digit += matches[-1]
        digits = first_digit + last_digit
        cal_vals.append(int(digits))
        print(matches, i, digits)

    total = sum(cal_vals)
    return total

print(updated_calval(lines))
