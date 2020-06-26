def duplicate_encode(word):
    counts = dict()
    for l in word.lower():
        counts[l] = counts.get(l,0) + 1

    for k,v in counts.items():
        if v > 1: counts[k] = ')'
        else: counts[k] = '('

    return ''.join(counts.get(x,'') for x in word.lower())

handler = open("random_strings.txt")
encoded = list()
for line in handler:
    encoded.append(duplicate_encode(line))
