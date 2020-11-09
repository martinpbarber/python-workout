""" exercise_010 """


def mysum(*args):
    """ Sum a variable number of arguments """
    result = None

    for arg in args:
        if result is None:
            # First parameter
            result = arg
        else:
            # All other arguments
            result += arg

    return result
