import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]],dtype=complex)
print(x)	
print("the no: of rows and columns" ,x.shape)
print("dimention", x.ndim)
x1= x.reshape(3, 2)
print("reshape the same array to 3X2")
print(x1)