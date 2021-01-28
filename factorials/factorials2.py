import itertools
import numpy as np
import sympy as sym
from fractions import Fraction

N = 15
results = []
for n in xrange(N + 1):
    result = []
    for k in xrange(n + 1):
        total = 0
        for t in itertools.combinations(range(n + 1), k):
            total += int(np.prod(t))
        result.append(total)
    results.append(result)

# (n + 1)! = (n + 1) * n! = n * n! + n!
# (n + 1)! = sum_k prod_c c(n, k) = 1 + (1 + ... + n) + ... + n!
# n! = (1/n) * (1 + (1+...+n) + ... + (n!/1+...+n!/n))


f = 1
for n, result in enumerate(results, start=1):
    # print(result)
    f *= n
    # ps = [Fraction(r, f) for r in reversed(result)]
    ps = [float(r) / float(f) for r in reversed(result)]
    vs = [i * p for i, p in enumerate(ps, start=1)]
    v = sum(vs)
    # print (ps)
    # print(vs)
    # print(v)
    print(n, float(v), np.log(n))
    # print([i * Fraction(r, f) for i, r in enumerate(reversed(result), start=1)])
    # print(sum([i * Fraction(r, f) for i, r in enumerate(reversed(result), start=1)]))

    # print(sum(result))
    # print(sum([Fraction(1, r) for r in result]))
    # print(sum([Fraction(1, result[i]) * (i + 1) for i in xrange(len(result))]))
    # print(sum([Fraction(1, result[i]) * i for i in xrange(len(result))]))
    # print(sum([len(result) * float(i + 1) / result[i] for i in xrange(len(result))]))
