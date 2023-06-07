def quick_sort(list):
    if len(list) < 2:
        return list
    pivo = list[0]
    smaller = [i for i in list[1:] if i <= pivo]
    bigger = [i for i in list[1:] if i > pivo]
    return quick_sort(smaller) + [pivo] + quick_sort(bigger)


def is_anagram(string_one, string_two):
    one_w = list(string_one.lower())
    two_w = list(string_two.lower())

    order_one_w = "".join(quick_sort(one_w))
    order_two_w = "".join(quick_sort(two_w))
    if (string_one == '' or string_two == ''):
        return order_one_w, order_two_w, False
    return order_one_w, order_two_w, order_one_w == order_two_w
