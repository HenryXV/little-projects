def solution(string):
    letters = ([str(letter) for letter in string])
    letters.reverse()
    return "".join(letters)
