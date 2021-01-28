N = 15
results = [[1]]
for i in xrange(N):
    results.append([len(results[i]) * a + b for a, b in zip([0] + results[i], results[i] + [0])])

for result in results:
    print(result)
