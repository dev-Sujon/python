def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for numeral in s[::-1]:
        value = roman_numerals[numeral]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


roman_numeral = "XIV"
integer_value = roman_to_int(roman_numeral)
print(integer_value)  # Output: 14
