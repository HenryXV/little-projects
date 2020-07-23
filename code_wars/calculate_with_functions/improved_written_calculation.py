#checks wich operation need to be done
def check_oper(data, int):
    items = [item for tuple in data for item in tuple]
    if items[0] == '+':
        return int + items[1]
    elif items[0] == '-':
        return int - items[1]
    elif items[0] == '*':
        return int * items[1]
    elif items[0] == '/':
        return int / items[1]

#uses optinal arguments to see if it's the left operand,
#if it's the right operand, returns the number itself
def zero(*options):
    if len(options) > 0:
        return int(check_oper(options, 0))
    else:
        return 0
def one(*options):
    if len(options) > 0:
        return int(check_oper(options, 1))
    else:
        return 1
def two(*options):
    if len(options) > 0:
        return int(check_oper(options, 2))
    else:
        return 2
def three(*options):
    if len(options) > 0:
        return int(check_oper(options, 3))
    else:
        return 3
def four(*options):
    if len(options) > 0:
        return int(check_oper(options, 4))
    else:
        return 4
def five(*options):
    if len(options) > 0:
        return int(check_oper(options, 5))
    else:
        return 5
def six(*options):
    if len(options) > 0:
        return int(check_oper(options, 6))
    else:
        return 6
def seven(*options):
    if len(options) > 0:
        return int(check_oper(options, 7))
    else:
        return 7
def eight(*options):
    if len(options) > 0:
        return int(check_oper(options, 8))
    else:
        return 8
def nine(*options):
    if len(options) > 0:
        return int(check_oper(options, 9))
    else:
        return 9

#return the operation signal and the number
#that is going to be needed for the operation
def plus(number):
    return '+', number
def minus(number):
    return '-', number
def times(number):
    return '*', number
def divided_by(number):
    return '/', number

print(seven(times(five())))
