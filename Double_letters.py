def double_letters(p):
    return any([a==b for a, b in zip(p, p[1:])])
print(double_letters('happy'))
print(double_letters('window'))