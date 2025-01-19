import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, -6, 7, 8],
              [-9, 10, 11, 12]])
a = np.delete(a, 0, 0)
a = np.delete(a, -1, 1)
print(a)
a[a <= 0] = a[a <= 0] * a[a <= 0]
print(a)