import cProfile
import matplotlib.pyplot as plt

from square_sum_sequences import NaiveSquareSumSequence, FastSquareSumSequence

SEED = 1
LENGTH = 2 * 10 ** 5

sequence = FastSquareSumSequence(seed=SEED, length=LENGTH).to_list()

# plt.plot(sequence)
# plt.show()

sss = FastSquareSumSequence(seed=SEED)
min = [SEED]
seq = [SEED]
max = [SEED]
win = [0.0]
min_streak = {SEED: 1}
for _ in xrange(1, LENGTH):
    if _ % (LENGTH / 10) == 0:
        print 10 * _ / (LENGTH / 10), _
    sss.append_next_value()
    seq.append(sss.last_value)
    next_min = min[-1]
    while next_min in sss.mapping:
        next_min += 1
    next_min -= 1
    min.append(next_min)
    if next_min in min_streak:
        min_streak[next_min] += 1
    else:
        min_streak[next_min] = 1
    next_max = max[-1]
    if sss.last_value > next_max:
        next_max = sss.last_value
    max.append(next_max)
    assert len(seq) == len(min)
    assert len(seq) == len(max)
    next_win = (max[-1] - min[-1]) / float(len(seq))
    if next_win > 0.3:
        next_win = 0.3
    win.append(next_win)

plt.plot(*zip(*sorted(min_streak.items())))

# plt.plot(seq)
# plt.plot(min)
# plt.plot(max)
# plt.plot(win)
plt.show()

# max_value = max(sequence)
# missing_values = [value for value in xrange(1, max_value + 1) if value not in sequence]
# min_missing_value = min(missing_values)
# missing_values_length_or_less = [value for value in missing_values if value <= LENGTH]
#
# print "Length: {}".format(LENGTH)
# print "Maximum value: {}".format(max_value)
# print "Minimum missing value: {}".format(min_missing_value)
# print "Number of missing values: {}".format(len(missing_values))
# print "Number of missing values length or less: {}".format(len(missing_values_length_or_less))
# print
# print "Maximum value as a proportion of length: {}".format(round(max_value / float(LENGTH), 2))
# print "Minimum missing value as a proportion of length: {}".format(round(min_missing_value / float(LENGTH), 2))
# print "Proportion of missing values length or less: {}".format(
#     round(len(missing_values_length_or_less) / float(LENGTH), 2))
