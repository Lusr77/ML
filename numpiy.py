import numpy as np
import time,sys
import matplotlib.pyplot as plt
# a=np.array([(1,2,4),(6,7,8)])
# print(a)
#-----Less Memory
s=range(1000)
print(sys.getsizeof(5)*len(s))
D=np.arange(1000)
print(D.size*D.itemsize)
#-----Faster
# size=100000
# list1=range(size)
# list2=range(size)
# nar1=np.arange(size)
# nar2=np.arange(size)
# start_time=time.time()
# result=[(x+y) for x,y in zip(list1,list2)]
# print("Lists:",(time.time()-start_time)*1000)
# start_time=time.time()
# result=nar1+nar2
# print((time.time()-start_time)*1000)
#---------Various Operation--------------->
ar2=np.array([(1,23,4),(4,5,6)])
print(ar2.ndim)#no of dimensions
print(ar2.itemsize)#byte size of data
print(ar2.dtype)#data type
print(ar2.size)#size of array total no of elements
print(ar2.shape)#no of rows and columns
# ar2=ar2.reshape(3,2)#--->Transpose
print(ar2)
print(ar2[0,1])#---slicing
print(ar2[0:,2])
a=np.linspace(1,2,5)#--Line Spacing
print(a)
print(ar2.max())#---Max element in numpy array
print(ar2.min())#--------Min element in numpy array
print(ar2.sum())#-------Sum of all elements in an numpy array
print(ar2.sum(axis=1))#--------axis==1 means sum of individual rows in an array
print(ar2.sum(axis=0))#------axis=0 means sum of indidivual columns in an array
print(ar2.mean())#---Mean of the array
print(ar2.std())#---Standard deviation (The quantity of a value that differs form the mean of the group) (x-x(bar))square/n-1
ar3=np.array([(1,2,3),(4,5,6)])
print(ar2+ar3)#add
print(ar2-ar3)#sub
print(ar2*ar3)#mull
print(ar2/ar3)#div
#-----Concatinating row wise and column wise
print(np.vstack((ar2,ar3)))#concatinating column wise verticalstack
print(np.hstack((ar2,ar3)))#concatinating row wise horizontalstack
print(ar2.ravel())#---converts whole numpy array into a single rowed array
#----------Numpy functions-------
ab=np.random.randn(1,2,3)#-----gives random distibuted values based on gussian rule
#----------Plotting sin and cosine or any other graphs using numpy and matplotlib
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)#y=np.cos(x) or tan(x) etc
# plt.plot(x,y)
# plt.show()
#---------exponential(epower(x)) and logarthamic(log(base10)) and natural log (log(base e)) using numpy
ar=np.array([1,2,3])
print(np.exp(ar))
print(np.log(ar))#---natural log
print(np.log10(ar))#-----logarthmic base 10
from math import s