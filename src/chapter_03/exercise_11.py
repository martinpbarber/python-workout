""" exercise_11 """
import operator


def alphabetize_names(people):
    """ Sort an array of dictionaries by 'first' and 'last' name """

    sorted_people = sorted(people, key=operator.itemgetter("last", "first"))
    return sorted_people
