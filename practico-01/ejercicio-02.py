def max_de_tres(a, b, c):
    return max(max(a, b), c)


print('max_de_tres(3, 2, 1) =', max_de_tres(3, 2, 1))
print('max_de_tres(1, 2, 3) =', max_de_tres(1, 2, 3))
print('max_de_tres(1, 3, 2) =', max_de_tres(1, 3, 2))
print('max_de_tres(2, 3, 1) =', max_de_tres(2, 3, 1))
print('max_de_tres(3, 3, 1) =', max_de_tres(3, 3, 1))
print('max_de_tres(1, 3, 3) =', max_de_tres(1, 3, 3))
print('max_de_tres(3, 1, 3) =', max_de_tres(3, 1, 3))
print('max_de_tres(3, 3, 3) =', max_de_tres(3, 3, 3))
