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


N = 16
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
        diffs.append([y-x for (x,y) in zip(diffs[-1], diffs[-1][1:])])
    for diff in diffs:
        print i, diff