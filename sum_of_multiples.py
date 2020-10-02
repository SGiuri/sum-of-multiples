def sum_of_multiples(limit, multiples):
    """

    :param limit: a positive integer
    :param multiples: a list containing integers
    :return: the sum of multiplese

    """

    all_multiples = set()
    if len(multiples) == 0:
        return 0

    for i in range(len(multiples)):
        if multiples[i] != 0:
            for m in range(multiples[i],limit,multiples[i]):
                all_multiples.add(m)
            else:
                all_multiples.add(0)
    whole_sum = sum(all_multiples)

    return whole_sum

