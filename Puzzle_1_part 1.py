# Puzzle 1

with open('input.txt', 'r') as string_file:
    lines = string_file.readlines()


def calibration_values(string):
    numbers = [str(i) for i in range(0, 10)]
    cal_values = []

    for i in range(len(string)):
        fl_digits = ''
        for j in string[i]:
            if j in numbers:
                fl_digits += j
        digit = fl_digits[0] + fl_digits[-1]
        cal_values.append(int(digit))

    sum_cal = sum(cal_values)
    return sum_cal


print(calibration_values(lines))
