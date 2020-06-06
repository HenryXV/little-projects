import random

boolean = True

while boolean:
    dice = input('how many faces does your dice have? ')
    rolls = input('how many rolls do you want? ')

    try:
        faces = int(dice)
        irolls = int(rolls)
    except:
        print('please, type a valid number in both questions')
        continue

    for d in range(irolls):
        print(random.randint(1, faces))

    again = input('do you want to roll another dice? Y/N ')
    if again.lower() == 'y':
        continue
    else:
        break
