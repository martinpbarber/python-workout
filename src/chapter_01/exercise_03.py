""" exercise_03 """
import statistics


PROMPT = "Enter 10 km run time: "


def run_timing():
    """ Calcute the average of the supplied 10 km run times"""
    run_times = []

    while True:
        run_time = input(PROMPT)
        if not run_time:
            break
        run_times.append(float(run_time))

    average = calculate_average(run_times)
    average = round(average, 2)
    return average


def calculate_average(run_times):
    """ Calculate the average, returning zero if count is zero """
    if len(run_times) == 0:
        average = 0
    else:
        average = statistics.mean(run_times)

    return average
