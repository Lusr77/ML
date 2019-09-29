import  pandas as pd
import numpy as np
arr=np.array([34,58,59,60,20])
dict_arr={'a':1,'b':2,'c':3}
se=pd.Series(dict_arr)
print(se)
print(se[0:])
ab=[1,2,3,5]
lm=[{'a':1,'b':2},{'c':3,'d':4}]
listx=pd.DataFrame(lm,index=['Mon','Tue' ])
print(listx)


