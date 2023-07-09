def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return "".join(merged)


def is_anagram(first_string, second_string):
    first_string = merge_sort(first_string.lower())
    second_string = merge_sort(second_string.lower())

    if len(first_string) == 0 or len(second_string) == 0:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)
