""" exercise_02 """


def mysum(*numbers):
    """ Sum a variable number of arguements """
    total = 0

    for number in numbers:
        total = total + number

    return total
