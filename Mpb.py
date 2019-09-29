import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')
# plt.plot([1,2,3],[4,5,1])
# plt.show()
x=[4,5,6]
y=[7,1,6]
plt.plot(x,y,label='line1',linewidth=5)
plt.title("Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xticks(range(0,6),('dan','brain','kan','man','ran','dan'))
plt.legend()
plt.grid(True,color='c')
plt.show()