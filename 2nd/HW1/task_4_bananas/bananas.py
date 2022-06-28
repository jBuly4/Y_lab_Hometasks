

from itertools import combinations


def bananas(s: str) -> set:
    """
    Returns all possible words 'banana' from the string
    :param s: input string
    :return: set of words bananas
    """
    result = set()
    # Your code here!
    for word_idx_combination in combinations(range(len(s)), len(s) - 6):
        lst = list(s)
        # print(word_idx_combination)
        for idx in word_idx_combination:
            lst[idx] = '-'

        temp_word = "".join(lst)
        if temp_word.replace('-', '') == 'banana':
            result.add(temp_word)

    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a", "b-ana--na",
                                "b---anana", "-bana--na", "-ba--nana", "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
