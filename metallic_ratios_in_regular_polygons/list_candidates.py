import math

ERROR_THRESHOLD = 10 ** -9
MAX_VERTICES = 10 ** 3

for n in xrange(4, MAX_VERTICES + 1):
    for k2 in xrange(2, n / 2 + 1):
        value2 = math.sin(math.pi * k2 / n)
        for k1 in xrange(1, k2):
            value1 = math.sin(math.pi * k1 / n)
            value = value2 / value1 - value1 / value2
            index = int(round(value))
            error = abs(value - index)
            if error > ERROR_THRESHOLD:
                continue
            print(n, k2, k1, index)
