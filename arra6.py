from numpy import *

arr1 = array(
    [
        [1,2,3,5,3,3],
        [4,5,6,6,8,3],
    ]
)

# print(arr1)
# print(arr1.dtype) #int64
# print(arr1.ndim) #2
# print(arr1.shape) #(3, 3)


# arr2 = arr1.flatten() #creating one dimational array [1 2 3 4 5 6]
# print(arr2)
# print(id(arr2)) #140100136783664


# arr3 = arr1.reshape() #TypeError: reshape() takes exactly 1 argument (0 given)


# arr3 = arr1.reshape(3,4)
# arr3 = arr1.reshape(2,3,2)
# print(arr3)

# m =matrix(arr1)
# print(m)

m1 = matrix('1,2,4; 5,6,7; 2,3,5')  # matrix array
m2 = matrix('2,4,4; 9,7,8; 2,4,8')  #multiply matrix is required to shame row no. and same coloumn and also same are another matrix
m3 = m1 + m2  #add the matrix
m4 = m1 * m2
print(m4)
# print(diagonal(m1))
# print(m1.min())
# print(m1.max())
# print(m1)