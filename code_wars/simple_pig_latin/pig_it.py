import re

def pig_it(text):

    #resolution step by step
    # pig_text = list()
    # for word in text.split():
    #     if re.match(r'[a-z]', word, re.I):
    #         pig_text.append(word[1:len(word)] + word[0] + 'ay')
    #     else:
    #         pig_text.append(word)
    # return ' '.join(pig_text)

    #one-line solution using list comp
    return [word[1:] + word[0] + 'ay' if re.match(r'[a-z]', word, re.I) else word for word in text.split()]

print(pig_it('Pig latin is cool !'))
