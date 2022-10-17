import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.ndim)
print("Item Size",a.itemsize, " in byte")
print("data type:", a.dtype)
print("Element Number:", a.size , " int ")
print("array size:", a.shape)

# to specify data type

b = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.int16) # dtype=np.other data type

print("Item Size",b.itemsize)
print("data type:", b.dtype)

print("Create ndim array with values zeros")
c= np.zeros((3,4))
print(c)

print("Create ndim array with values zeros")
d= np.ones((3,4))
print(d)

# arange function alternative to range function in python
for i in np.arange(13):
    print(i)


# Return evenly spaced numbers over a specified interval
print(np.linspace(1,5,10))


# To reshape array
print(c.reshape(4,3))


# two dimension to one dimension array return new array
print(d.ravel())


# Math function in Numpy 

#Minimum and maximum number in array
print("Minimum number: ",a.min())
print("Maximum number: ",a.max())

# sumation of array
print("Sumation: ",a.sum())

# collumn sumation
print("Sumation: ",a.sum(axis=0))

#row sumation
print("Sumation: ",a.sum(axis=1))

#Squart root on every element
print("Squart root ",np.sqrt(a))

#Standard division
print("Standard division",np.std(a))

#dot product 

print(a.dot(b))
#or
print(a@b)

#basic math operation
print(a*2)
print(a+2)
print(a/2)
print(a-2)


#Indexing and slicing in Numpy:
print(a[:2,:2])

#flatter the array
for i in a.flat:
    print(i)

# Up down stack or add 
print(np.vstack((a,b)))

# Side by Side stack or add 
print(np.hstack((a,b)))

# Side by Side stack or add 
print(np.hstack((a,b)))

# horizontal splite
print(np.hsplit(a,3))

# vartically splite
print(np.vsplit(a,3))


# create array very easly
array = np.arange(12).reshape(3,4)
print(array)


# create boolean array 
array1 = a > 4
print(array1)

print(a[array1])
b[array1]=1
print(b)


#Iterate numpy array

array3 = np.arange(12).reshape(3,4)
for i in array3.flatten():
    print(i)
# c order fortran order external flags for column wise going
for element in np.nditer(a,order='F',flags=["external_loop"]):
    print(element)

# Read write array

for element in np.nditer(a,op_flags=['readwrite']):
    element[...] = element ** 2

print(a)

#print 2 array simultaneously
array4 = np.arange(12).reshape(3,4)

for x,y in np.nditer([a,b]):
    print(x,y)