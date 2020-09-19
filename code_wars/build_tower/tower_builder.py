def tower_builder(n_floors):
    tower = list(['*'])
    floor = 1

    while n_floors > 1:
        tower.append((floor + 2) * '*')
        n_floors = n_floors - 1
        floor = floor + 2

    return ['{:^{l}}'.format(f, l=floor) for f in tower]

print(tower_builder(10))
