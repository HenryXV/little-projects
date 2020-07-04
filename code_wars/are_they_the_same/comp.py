def comp(a1, a2):
    try:
        if sorted(x ** 2 for x in a1) == sorted(a2): return True
        else: return False
    except:
        return False


a1 = [90, 6, 62, 24, 82, 65, 2]
a2 = [8100, 36, 3845, 576, 6724, 4225, 4]
print(comp(a1,a2))
