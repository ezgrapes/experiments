import matplotlib.pyplot as plt

MAX_DIFFERENCE = 10 ** 3

# n^2 - (n-1)^2 = n^2 - (n^2 - 2n + 1) = n^2 - n^2 + 2n - 1 = 2n - 1
MAX_INTEGER = (MAX_DIFFERENCE + 1) / 2

results = {}
for n in xrange(0, MAX_INTEGER + 1):
    for m in xrange(0, n + 1):
        difference = n ** 2 - m ** 2
        pair = (n, m)
        if not difference in results:
            results[difference] = []
        results[difference].append(pair)

graph = []
for key in xrange(1, MAX_DIFFERENCE + 1):
    if not key in results:
        results[key] = []
    graph.append(len(results[key]))

plt.plot(graph)
plt.show()
