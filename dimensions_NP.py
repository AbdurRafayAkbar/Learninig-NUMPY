import numpy as np

# ZERO DIMESNIONAL ARRAYS

array=np.array("A")
print(array.ndim)

# ONE DIMESNIONAL ARRAYS

array=np.array(["A","B","C"])

print(array.ndim)

# TWO DIMENSIONAL ARRAYS

array = np.array([["A","B","C"],
                 ["D","E","F"],])

print(array.ndim)

# THREE DIMENSIONALS ARRAYS

array = np.array([[["A","B"],
                   ["C","D"],
                   ["E","F"]]])

print(array.ndim)