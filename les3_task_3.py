import les3_task_1 as t1
import numpy as np

x0 = 0
y0 = 0
V0x = 10
V0y = 5

results = []

for t in range(6):
    x = x0 + V0x*t
    y = y0 + V0y*t - (t1.g * t**2) / 2
    results.append([t, x, y])

new_results = np.array(results)
print(new_results)