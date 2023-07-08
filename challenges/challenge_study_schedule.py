def not_int(value):
    return not all(isinstance(elem, int) for elem in value)


def study_schedule(permanence_period, target_time):
    if not_int([target_time]):
        return None

    frequency = 0

    for i in permanence_period:
        if not_int(i):
            return None
        if i[0] <= target_time <= i[1]:
            frequency += 1

    return frequency


study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5)
