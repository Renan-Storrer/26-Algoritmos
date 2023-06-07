def letter_after(word, index_l, index_h):
    if index_l >= index_h:
        return True
    if word[index_l] != word[index_h]:
        return False
    return letter_after(word, index_l + 1, index_h - 1)


def is_palindrome_recursive(word, index_l, index_h):
    if len(word) == 0:
        return False
    return letter_after(word, index_l, index_h)