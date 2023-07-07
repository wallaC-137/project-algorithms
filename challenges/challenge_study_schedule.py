def is_none(value):
    return None in value


def not_int(value):
    return not all(isinstance(elem, int) for elem in value)


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    frequency = 0

    for i in permanence_period:
        if is_none(i) or not_int(i):
            return None
        if i[0] <= target_time <= i[1]:
            frequency += 1

    return frequency
