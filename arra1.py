#interger Array

from array import *

# vals = array('i', [5,9,8,5,4]) # NOt Error
# vals = array('i', [5,9,8.5,5,4]) #become a error (TypeError: integer argument expected, got float)

# vals = array('I', [5,-9,8,-5,4])  # Become a error (OverflowError: can't convert negative value to unsigned int)
# print(vals)


# vals = array('i', [5,-9,8,-5,4]) # (140125596097136, 5)
# print(vals.buffer_info()) # address :- 140125596097136 size:- 5,

# vals = array('i', [5,-9,8,-5,4])
# print(vals.typecode) #print is "i"



# vals = array('i', [5,-9,8,-5,4])
# val = vals.reverse()
# print(vals)


# vals = array('i', [5,-9,8,-5,4])
# val = vals.reverse()
# print(vals[2])



# vals = array('i', [5,-9,8,-5,4])
# # print(vals[0])
# for i in vals:
#     print(i)



# vals = array('i', [5,-9,8,-5,4])
# for i in range(len(vals)):
#     print(i)


# vals = array('u', ['a','e','i','l','o','u'])
# print(vals)

# vals = array('i',[5,6,7,8,9,2])

# newArray = array(vals.typecode, (a*a for a in vals))

# # for i in newArray:
# #     print(i)

# i = 0 #
# while i < len(newArray):
#     print(newArray[i])
#     i = i+ 1