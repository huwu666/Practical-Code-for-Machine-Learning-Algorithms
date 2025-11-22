from random import normalvariate
import time
import numpy as np

n = 10000000
start = time.time()
samples = [normalvariate(0, 1) for _ in range(n)]
times = np.random.normal(size = n)
end = time.time()
print(end - start)