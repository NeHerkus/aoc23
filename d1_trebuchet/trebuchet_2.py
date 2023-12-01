def replace_spelt_digits(line):
    return line.replace('one', 'o1e')\
        .replace('two', 't2o')\
        .replace('three', 't3e')\
        .replace('four', '4')\
        .replace('five', '5e')\
        .replace('six', '6')\
        .replace('seven', '7n')\
        .replace('eight', 'e8t')\
        .replace('nine', 'n9e')


def count_sum(lines):
    calibration_sum = 0
    for line in lines:
        digits = list(filter(lambda x: x.isdigit(), [*line]))
        calibration_sum += 10 * int(digits[0]) + int(digits[-1])
    return calibration_sum


lines = open('calibration document.txt', "r").read().split("\n")
print(count_sum([replace_spelt_digits(w) for w in lines]))
