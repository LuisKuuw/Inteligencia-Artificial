import numpy as np
import heapq
import sys
import time

time_heapify = np.zeros(8)
time_extract = np.zeros(8)

for i in range(8):
    elements = pow(10, i)
    
    a = list(np.random.randint(low=sys.maxint, size=elements))

    heapq.heapify(a)

    for j in range(elements):

        heapq.heappop(a)
