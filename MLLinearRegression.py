import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

data=pd.read_csv('data2.csv')
array=['TV','radio','newspaper']
x=data[array]
y=data.sales
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=3)
linearreg=LinearRegression()
linearreg.fit(x_train,y_train)

y_predict=linearreg.predict(x_test)
#print(y_predict)
print(np.sqrt(metrics.mean_squared_error(y_test,y_predict)))

plt.plot(x_test['TV'],y_predict)
plt.plot(x_test['TV'],y_test,'r.')
plt.show()
