import numpy as np

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

#use zip method to map the similar indices of the 4 lists so as to use them as a single entity

#np.all() function tests whether all array elements along the mentioned axis evaluate to True
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.all(array)}')
