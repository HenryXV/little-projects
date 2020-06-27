import string

def is_pangram(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    translation = s.translate(str.maketrans('','',(string.punctuation + string.digits)))
    pangram = dict()
    for l in translation.lower().replace(' ', ''):
        pangram[l] = pangram.get(l,0) + 1
    letters = [str(k) for k,v in pangram.items()]

    comparison = [x for x in letters + alphabet if x not in letters]

    if not comparison: return True
    else: return False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
