import numpy as np
# concatenate arrays
arr1=np.array([[1,2,3],[3,4,5],[6,7,8]])
arr2=np.array([[9,10,11],[12,13,14],[15,16,17]])
arr3=np.array([[18,19,20],[21,23,24],[25,26,27]])
newarr=np.concatenate((arr1,arr2,arr3))
print(newarr)
ar=np.array(ndmin=2,object=[])
ar=np.append(arr=ar,values=[[1,2,3,4],[1,4,6,7]])
print(ar.ndim)
k="gtdey"
b=hash(k)
print(b)