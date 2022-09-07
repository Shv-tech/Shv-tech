 import array


array import arrayfrom
from sklearn.datasets import load_digits

digits_data = load_digits()
digits_data.data.shape
import matplotlib.pyplot as plt
plt.matshow(digits_data.images[0])
plt.show(1)
digits_data.images[0]
array([[ 0.,   0.,   5.,    13.,    9.,     1.,     0.,    0.],
       [ 0.,   0.,  13.,    15.,   10.,    15.,     5.,    0.],
       [ 0.,   3.,  15.,     2.,    0.,    11.,     8.,    0.],
       [ 0.,   4.,  12.,     0.,    0.,     8.,     8.,    0.],
       [ 0.,   5.,   8.,     0.,    0.,     9.,     8.,    0.],
       [ 0.,   4.,  11.,     0.,    1.,    12.,     7.,    0.],
       [ 0.,   2.,  14.,     5.,   10.,    12.,     0.,    0.],
       [ 0.,   0.,   6.,    13.,   10.,     0.,     0.,    0.]])
 
 images = list(zip(digits_data.images, digits_data.target))
 plt.figure(figsize=(4,4))
