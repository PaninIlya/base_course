import numpy as np
import les3_task_1 as t1

h = 100
a = 45
b = 35

V = np.sqrt((t1.g * h* np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(b)*np.tan(a))))
print(V)

from les3_task_1 import h
from les3_task_1 import k
from les3_task_1 import p
from les3_task_1 import e

T = 200
E = 300

N = 2/np.sqrt(p) * np.sqrt(h) * (k*T)**(1.5) * e**E/k*T * E**(T/2)
print(N)