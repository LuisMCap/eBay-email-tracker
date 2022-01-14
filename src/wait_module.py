import time
from random import choice
import numpy as np


def calculate_total_wait_time(down_time_hours):
    down_time_seconds = down_time_hours * 60 * 60

    variance_in_seconds = np.arange(-600, 660, 60)
    seconds_added_or_subtracted = choice(variance_in_seconds)

    down_time_seconds += seconds_added_or_subtracted

    return down_time_seconds


def sleep_time(down_time_seconds):
    time.sleep(down_time_seconds)
