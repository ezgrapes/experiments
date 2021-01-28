import sympy as sym


def get_term(number):
    degree = 0
    product = 1
    index = 0
    while number != 0:
        number, bit = divmod(number, 2)
        if bit:
            degree += bit
            product *= index + 1
        index += 1
    return degree, product


def get_coefficients(n):
    coefficients = [0] * (n + 1)
    for i in xrange(2 ** n):
        degree, product = get_term(number=i)
        coefficients[degree] += product
    return coefficients


N = 17
slices = []
for i in xrange(N):
    slices.append([])
for i in xrange(N):
    coefficients = get_coefficients(n=i)
    for j, v in enumerate(coefficients):
        slices[j].append(v)

for i in xrange(N):
    diffs = []
    diffs.append(slices[i])
    while len(diffs[-1]) > 1 and diffs[-1][0] != diffs[-1][1]:
        diffs.append([y - x for (x, y) in zip(diffs[-1], diffs[-1][1:])])
    if len(diffs[-1]) > 1:
        for diff in diffs:
            print i, diff
    # print i, get_coefficients(n=i+1)
    degree = 2 * i
    a = sym.Matrix([[j ** k for k in xrange(degree + 1)] for j in range(i, i + degree + 1)])
    b = sym.Matrix(slices[i][:degree + 1])
    if len(b) != degree + 1:
        break
    x = a.solve(b)
    if a * x == b:
        f = sym.factorial(2 * i)
        y = f * x
        g = sym.gcd([element for element in y])
        n = y / g
        print i, x
        print i, f
        print i, y
        print i, g
        print i, n
    a = sym.Matrix([[j ** k for k in xrange(degree + 1)] for j in range(degree + 1)])
    b = sym.Matrix(slices[i][:degree + 1])
    if len(b) != degree + 1:
        break
    x = a.solve(b)
    if a * x == b:
        f = sym.factorial(2 * i)
        y = f * x
        g = sym.gcd([element for element in y])
        n = y / g
        print i, x
        print i, f
        print i, y
        print i, g
        print i, n
