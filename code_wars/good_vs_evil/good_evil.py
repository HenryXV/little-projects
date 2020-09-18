def goodVsEvil(good, evil):

    good_side = (1,2,3,3,4,10)
    evil_side = (1,2,2,2,3,5,10)

    good_worth = [int(i) for i in good.split(' ')]
    evil_worth = [int(i) for i in evil.split(' ')]

    for i, worth in enumerate(good_worth):
        good_worth[i] = worth * good_side[i]
    for i, worth in enumerate(evil_worth):
        evil_worth[i] = worth * evil_side[i]

    if sum(good_worth) > sum(evil_worth):
        return "Battle Result: Good triumphs over Evil"
    elif sum(good_worth) < sum(evil_worth):
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print(goodVsEvil('1 1 1 1 1 1', '1 0 1 1 1 1 1'))
