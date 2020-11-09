""" exercise_03 """


PROMPT = "Enter a hex number to convert: "


def hex_output():
    """ Convert hexadecimal number to decimal """

    hex_number = input(PROMPT)

    decimal_number = 0
    for (place, value) in enumerate(reversed(hex_number)):
        print(f"value: {value}")
        print(f"place: {place}")
        decimal_number += int(value, 16) * (16 ** place)

    return decimal_number
