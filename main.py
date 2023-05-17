def covert_int_to_roman(num: int) -> int:
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman = ''
    for value, symbol in roman_numerals.items():
        while num >= value:
            roman += symbol
            num -= value

    return roman


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    roman_numeral = covert_int_to_roman(number)
    print(f"The Roman numeral representation of {number} is: {roman_numeral}")
