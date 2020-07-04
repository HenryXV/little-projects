import random
random_number = random.randint(0, 10)
while True:
    guess = input('I dare you to guess the number I am thinking!')
    try:
        number = int(guess)
    except:
        print("That's not a number!")
        continue
    if random_number == number:
        print("Wow, you're really good at guessing!")
        break
    else:
        print("Well, don't feel bad for giving a wrong answer, it's all about luck. I'll give you another opportunity.")
        continue
