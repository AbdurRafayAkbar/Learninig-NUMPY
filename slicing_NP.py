import numpy as np
array_2d=np.array([
    ["A","B","C","D"],
    ["E","F","G","H"],
    ["I","J","K","L"],
    ["M","N","O","P"],
    ["Q","R","S","T"],
    ["U","V","W","X"]])



# print(array_2d[1:4])


#ACCESSING 2nd-COLUMN only

print(array_2d[:,1]) #: means selecting all rows. 1 means 1 element of each column, It starts from 0

#ACCESSING 1st,2nd and 3rd column

print(array_2d[:,0:3]) #0:3 means select from 0index to 3rd index

#selcting "C,D" and "G,H"

print(array_2d[0:2,2:4])