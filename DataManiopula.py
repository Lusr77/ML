import pandas as pd
import matplotlib.pyplot as plt
import numpy
plt.figure(figsize=(50,50))
dt=pd.read_csv('food-price-index-apr19-seasonally-adjusted-csv-tables.csv')
print(dt.shape)
print(dt.dtypes)
print(dt.head(5))
print(dt.describe())
#---->Values having greater than 1050 in data set DataValues
# selected_list=dt.loc[:,['Period','Data_value']]
# for i in selected_list.itertuples():
#    if i[2]>1050:
#        print(i)
#------------>Correlation b/w period and data_vvalue
# selected_list=dt.loc[:,['Period','Data_value']]
# x=numpy.array(selected_list['Period'])
# y=numpy.array((selected_list['Data_value']))
# plt.bar(x,y)
# plt.ylim(0,700)
# plt.show()