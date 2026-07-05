import numpy as np

# # ZERO DIMESNIONAL ARRAYS

# array=np.array("A")
# print(array.ndim)

# # ONE DIMESNIONAL ARRAYS

# array=np.array(["A","B","C"])

# print(array.ndim)

# # TWO DIMENSIONAL ARRAYS

# array = np.array([["A","B","C"],
#                  ["D","E","F"],])

# print(array.ndim)

# # THREE DIMENSIONALS ARRAYS

# array = np.array([[["A","B"],
#                    ["C","D"],
#                    ["E","F"]]])

# print(array.ndim)

#<-------------------------------------------------------------------------------------------->

#Multi Dimensional Indexing. Getting values from he arrays

# 2 Dimensional Array
array =np.array([
    ["A","B","C","D"],
    ["E","F","G","H"],
    ["I","J","K","L"],
    ["M","N","O","P"],
    ["Q","R","S","T"],
    ["U","V","W","X"]])

#print(array(rows,columns))
print(array[5,3])

# 3Dimensional Array

Three_D_array=np.array([[
    ["A","B"],
    ["C","D"],
    ["K","L"]
],
[
    ["E","F"],
    ["G","H"],
    ["I","J"],

]
])
print(np.shape(Three_D_array))

