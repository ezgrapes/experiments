import cProfile
import matplotlib.pyplot as plt

from square_sum_sequences import NaiveSquareSumSequence, FastSquareSumSequence

LENGTH = 5 * 10 ** 5

sss = FastSquareSumSequence()
seq = [1]
min_values = [1]
min_indices = [0]
max_values = [1]
max_indices = [0]
for _ in xrange(1, LENGTH):
    if _ % (LENGTH / 10) == 0:
        print 10 * _ / (LENGTH / 10), _
    # Update sequence as data structure
    sss.append_next_value()
    # Update sequence as a list
    seq.append(sss.last_value)
    # Find next min value and update
    next_min_value = min_values[-1]
    while next_min_value in sss.mapping:
        next_min_value += 1
    next_min_value -= 1
    if min_values[-1] == next_min_value:
        min_indices.append(min_indices[-1])
    else:
        min_indices.append(seq.index(next_min_value))
    min_values.append(next_min_value)
    # Find next max value and update
    next_max_value = max_values[-1]
    if sss.last_value > next_max_value:
        next_max_value = sss.last_value
    if max_values[-1] == next_max_value:
        max_indices.append(max_indices[-1])
    else:
        max_indices.append(_)
    max_values.append(next_max_value)
    # Check lengths
    assert len(seq) == len(min_values)
    assert len(seq) == len(max_values)
    assert len(seq) == len(min_indices)
    assert len(seq) == len(max_indices)

# plt.plot(seq)
# plt.plot(min_values)
# plt.plot(max_values)
# plt.show()

# plt.plot(xrange(LENGTH))
# plt.plot(min_indices)
# plt.plot(max_indices)
# plt.show()

plt.plot([i / 10 for i in xrange(LENGTH)])
plt.plot([i - min_indices[i] for i in xrange(LENGTH)])
plt.plot([i - max_indices[i] for i in xrange(LENGTH)])
plt.show()
