import itertools

def longest(s1, s2):
    letters = dict()
    alphabet = list()

    for (l1,l2) in itertools.zip_longest(s1,s2):
        letters[l1] = letters.get(l1,1)
        letters[l2] = letters.get(l2,1)
        if None in letters:
            letters.pop(None)

    for k,v in letters.items():
        if v == 1:
            alphabet.append(k)

    return ''.join(sorted(alphabet))



print(longest("aretheyhere", "yestheyarehere"))
