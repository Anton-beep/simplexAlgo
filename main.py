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


def print_matrix(matrix):
    for row in matrix:
        print(list(map(lambda x: round(x, 3), row)))


def simplex(_input):
    if is_all_positive(_input[-1]):
        print("all elements in the objective\nrow are positive")
        if input() != '':
            return

        for i in range(len(_input[0])):
            one_ind = -1
            count_non_zero = 0
            for ind, el in enumerate(_input[:-1]):
                if el[i] != 0:
                    count_non_zero += 1
                if el[i] == 1:
                    one_ind = ind

            if count_non_zero == 1 and one_ind != -1:
                print("found a basic variable in\ncolumn {}: {}".format(i, round(_input[one_ind][-1], 3)))
                input()
        print("simplex end")
        return

    # find smallest in the objective function for pivot column
    smallest_ind = find_smallest_index(_input[-1])
    print("smallest in the objective row\n-> ind: {}, el: {}".format(smallest_ind, round(_input[-1][smallest_ind], 3)))
    if input() != '':
        return
    # find the smallest ratio to find the pivot element
    ratio = []
    for el in _input[:-1]:
        if el[smallest_ind] == 0:
            ratio.append(0)
            continue
        ratio.append(el[-1] / el[smallest_ind])

    print("ratios for the pivot column:\n{}".format(
        [round(el, 3) for el in ratio],
    ))
    if input() != '':
        return

    # check if ratios are negative
    if all(map(lambda x: x < 0, ratio)):
        print("all ratios are negative")
        print("no solution")
        return

    smallest_ratio = find_smallest_index_positive(ratio)
    print("smallest ratio -> ind: {},\nel: {}".format(smallest_ratio, round(ratio[smallest_ratio], 3)))
    if input() != '':
        return

    # now make all elements in a pivot column, except pivot element, zeroes
    print("make all elements in a pivot\ncolumn, except pivot \nelement, zeroes")
    if input() != '':
        return
    pivot_element = _input[smallest_ratio][smallest_ind]

    print(
        "make pivot element equal to 1:\nR{} -> R{} / {}".format(smallest_ratio + 1, smallest_ratio + 1, round(pivot_element, 3)))
    if input() != '':
        return
    for i in range(len(_input[smallest_ratio])):
        _input[smallest_ratio][i] = round(_input[smallest_ratio][i] / pivot_element, 7)

    for ind, el in enumerate(_input):
        if ind == smallest_ratio:
            continue

        coef = el[smallest_ind]
        print("R{} -> R{} - {} * R{}".format(ind + 1, ind + 1, round(coef, 3), smallest_ratio + 1))
        if input() != '':
            return
        for i in range(len(el)):
            _input[ind][i] = round(_input[ind][i] - _input[smallest_ratio][i] * coef, 7)

    print_matrix(_input)
    simplex(_input)


# example = [
#    [1, 4, 1, 0, -5, 8],
#    [1, 1, 0, 1, -2, 12],
#    [-1, -2, 0, 0, 3, 0],
# ]


example = [
    [3, 6, 1, 0, 0, 10000],
    [7, 4, 0, 1, 0, 15000],
    [-6, -5, 0, 0, 1, 0]
]

# to make an example, write
# first columns as
# coefficients of the
# variables (x, y...), then
# slack variables (s1, s2...),
# then problem column (all
# zeroes except objective
# function) (P), then right
# hand side values (R.H.S.).
# Last row is the objective
# function.

simplex(example)
