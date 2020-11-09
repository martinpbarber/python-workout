""" exercise_08 """


def strsort(string):
    """ Sort the letters in a string """
    sorted_list = sorted(string)

    sorted_string = "".join(sorted_list)
    return sorted_string
