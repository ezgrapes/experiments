import fractions
import math

DENOMINATOR = 2520 # lcm(1, 2, ..., 10)
ERROR_THRESHOLD = 10 ** -9 / DENOMINATOR
MAX_VERTICES = 10 ** 3

for n in xrange(4, MAX_VERTICES + 1):
    for k2 in xrange(2, n / 2 + 1):
        gcd2 = fractions.gcd(n, k2)
        value2 = math.sin(math.pi * k2 / n)
        for k1 in xrange(1, k2):
            gcd = fractions.gcd(gcd2, k1)
            if gcd > 1:
                continue
            value1 = math.sin(math.pi * k1 / n)
            value = value2 / value1 - value1 / value2
            index = round(DENOMINATOR * value) / DENOMINATOR
            error = abs(value - index)
            if error > ERROR_THRESHOLD:
                continue
            print(n, k2, k1, index)
