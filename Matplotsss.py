import matplotlib.pyplot as plt
import numpy
#a rr=numpy.linspace(0,20,5)
# plt.plot(arr)
# plt.show()
# y_value=[1, 2, 3]
# x_value=[10,20,30]
# plt.plot(x_value,y_value)
# plt.show()
# x=range(5)
# plt.plot(x,[i**2 for i in x],label="Squared")
# plt.plot(x,[i**3 for i in x],label="Cubed")
# plt.grid(True)
# plt.axis([0,3,0,5])
#--->xlim plt.xlim(0,3) ---->plt.ylim(0,5)
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title('Learning MatplotLib')
# plt.legend()
# plt.savefig('firstplot.png')
# plt.show()
#----Histogram
# x=numpy.random.randn(2,3)
# print(x)
# y=numpy.random.randn(2,2)
#print(y)
# plt.show()
# plt.hist(x,7)
#-----Bar Graph===
# plt.bar([1.5,2.6,4.8],[40,55,80])
#plt.show()
# ex_dict={'a':1,'b':2,'c':7}
# for i,key in enumerate(ex_dict):
#    plt.bar(i, ex_dict[key])
# plt.xticks(numpy.arange(len(ex_dict)),ex_dict.keys())
# plt.show()
#-----Pie-Chart-------
# plt.figure(figsize=(3,3))
# plt.pie([3,4,5],labels=['C++','Java','Pytho'])
# plt.show()
#--------scatter-plot-------
x=numpy.random.randn(22)
y=numpy.random.randn(22)
print(x,y)
plt.scatter(x,y)
plt.show()