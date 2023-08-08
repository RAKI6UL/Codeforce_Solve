def rearrange_sum(s):
    digits = [int(char) for char in s if char.isdigit()]

    sorted_digits = sorted(digits)

    new_sum = "+".join(str(digit) for digit in sorted_digits)

    return new_sum

input_sum = input()

print(rearrange_sum(input_sum))
