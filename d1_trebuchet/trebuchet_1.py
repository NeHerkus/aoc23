lines = open('calibration document.txt', "r").read().split("\n")
calibration_sum = 0
for line in lines:
    digits = list(filter(lambda x: x.isdigit(), [*line]))
    calibration_sum += 10 * int(digits[0]) + int(digits[-1])
print(calibration_sum)
