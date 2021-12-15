from numpy import *

# arr1 = array([1,2,3,4,5,6,7,8,9]) #count no. of value in array
# arr2 = array([10,11,12,13,14,15,16,17,18]) #same no. of this array if you are can't add same value show the error like (ValueError: operands could not be broadcast together with shapes (9,) (6,) )
# newArray = arr1 + arr2
# print(newArray) #[11 13 15 17 19 21 23 25 27]




# arr = array([1,2,3,4,5,6,7,8,9])
# arr1 = array([10,11,12,13,14,15,16,17,18])
# print("sin value of the array:- ", sin(arr))
# print("================================================================") 
# print("cos value of the array:- ", cos(arr))
# print("================================================================") 
# print("tan value of the array:- ", tan(arr))
# print("================================================================") 
# print("squre root of the array:- ", sqrt(arr))
# print("================================================================") 
# print("squre of the array:- ", (arr)**2)
# print("================================================================") 
# print("sum of the array:- ", sum(arr))
# print("================================================================") 
# print("max of the array:- ", max(arr))
# print("================================================================") 
# print("min of the array:- ", min(arr))
# print("================================================================") 
# print("Adding all the array in newArray Fields", concatenate([arr, arr1]))
# print("================================================================") 


# # # arr2 = arr 
# # print("Coping the Array", arr2)
# # print("================================================================") 
# # print("print the array addres:- ", id(arr2))
# # print("print the array addres:- ", id(arr))

# print("================================================================") 
# arr2 = arr.view()
# print("print the array addres:- ", id(arr2))
# print("print the array addres:- ", id(arr))

# print("================================================================") 
# print("================================================================") 
# print("There are two type of copy in array 1. shallow copy and 2. deep copy")
# print("================================================================") 



# arr = array([1,2,3,4,5,6,7,8,9])
# arr[1] = 8 #shallow copy
# print(arr)



# arr = array([1,2,3,4,5,6,7,8,9])
# arr[1] = 8 
# print(arr)

#shallow copy is using view() function and deep copy is using copy() function
# arr = array([1,2,3,4,5,6,7,8,9])
# arr2 = arr.copy()
# print(arr2)
# print(arr)
# print(id(arr))
# print(id(arr2))
