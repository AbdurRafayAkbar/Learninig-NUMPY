import numpy as np

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

final=Three_D_array[0,1,1] + Three_D_array[1,2,0] + Three_D_array[1,1,0]
print(final)