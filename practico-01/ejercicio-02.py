def max_de_tres(a, b, c):
    return max(max(a, b), c)


assert max_de_tres(3, 2, 1) == 3
assert max_de_tres(1, 2, 3) == 3
assert max_de_tres(1, 3, 2) == 3
assert max_de_tres(2, 3, 1) == 3
assert max_de_tres(3, 3, 1) == 3
assert max_de_tres(1, 3, 3) == 3
assert max_de_tres(3, 1, 3) == 3
assert max_de_tres(3, 3, 3) == 3
