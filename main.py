from pprint import pprint


def is_all_positive(in_list):
    # in this function 0 is considered as positive
    return all(map(lambda x: x >= 0, in_list))


def find_smallest_index(in_list):
    min_val = in_list[0]
    min_index = 0
    for ind, el in enumerate(in_list):
        if el < min_val:
            min_val = el
            min_index = ind

    return min_index


def find_smallest_index_positive(in_list):
    min_val = in_list[0]
    min_index = 0
    for ind, el in enumerate(in_list):
        if min_val > el > 0 or min_val <= 0:
            min_val = el
            min_index = ind

    return min_index


def simplex(input):
    if is_all_positive(input[-1]):
        print("all elements in the objective row are positive")

        for i in range(len(input[0])):
            one_ind = -1
            count_non_zero = 0
            for ind, el in enumerate(input[:-1]):
                if el[i] != 0:
                    count_non_zero += 1
                if el[i] == 1:
                    one_ind = ind

            if count_non_zero == 1 and one_ind != -1:
                print(f"found a basic variable in column {i}: {input[one_ind][-1]}")
        print("simplex end")
        return

    # find smallest in the objective function for pivot column
    smallest_ind = find_smallest_index(input[-1])
    print(f"smallest in the objective row -> ind: {smallest_ind}, el: {input[-1][smallest_ind]}")
    # find the smallest ratio to find the pivot element
    ratio = []
    for el in input[:-1]:
        if el[smallest_ind] == 0:
            ratio.append(0)
            continue
        ratio.append(el[-1] / el[smallest_ind])

    print(f"ratios for the pivot column: {ratio}")

    # check if ratios are negative
    if all(map(lambda x: x < 0, ratio)):
        print("all ratios are negative")
        print("no solution")
        return

    smallest_ratio = find_smallest_index_positive(ratio)
    print(f"smallest ratio -> ind: {smallest_ratio}, el: {ratio[smallest_ratio]}")

    # now make all elements in a pivot column, except pivot element, zeroes
    print("make all elements in a pivot column, except pivot element, zeroes")
    pivot_element = input[smallest_ratio][smallest_ind]

    print(f"make pivot element equal to 1: R{smallest_ratio + 1} -> R{smallest_ratio + 1} / {pivot_element}")
    for i in range(len(input[smallest_ratio])):
        input[smallest_ratio][i] = round(input[smallest_ratio][i] / pivot_element, 7)

    for ind, el in enumerate(input):
        if ind == smallest_ratio:
            continue

        coef = el[smallest_ind]
        print(f"R{ind + 1} -> R{ind + 1} - {coef} * R{smallest_ratio + 1}")
        for i in range(len(el)):
            input[ind][i] = round(input[ind][i] - input[smallest_ratio][i] * coef, 7)

    pprint(input)
    simplex(input)


# example = [
#    [1, 4, 1, 0, -5, 8],
#    [1, 1, 0, 1, -2, 12],
#    [-1, -2, 0, 0, 3, 0],
# ]


example = [
    [1, 1, 1, 1, 0, 0, -3, 59],
    [2, 0, 3, 0, 1, 0, -5, 75],
    [0, 1, 6, 0, 0, 1, -7, 54],
    [-2, -1, -3, 0, 0, 0, 6, 0],
]

# to make an example, write first columns as coefficients of the variables (x, y...), then slack variables (s1, s2...),
# then sum of the coefficients times -1 (W or A), then right hand side values (R.H.S.).
# Last row is the objective function.

simplex(example)
