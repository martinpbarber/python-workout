""" exercise_09 """


def firstlast(sequence):
    """ Return the first and last item in a sequence """

    # Slices handle empty sequences properly
    # and ensure a consistent type is returned
    first_item = sequence[:1]
    last_item = sequence[-1:]
    return first_item + last_item
