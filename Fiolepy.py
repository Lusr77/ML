'''
This help for Doxs
'''
# fob=open("MyFirstPyFile.txt","w+")
# for i in range(0,10):
  #  fob.write("\n JESUS")


# fob=open("MyFirstPyFile.txt","r")
# for i in range(0,9):
 #   print(fob.read(7))
# os.rename("MyFirstPyFile.txt","CopiedPyFile.txt")
#os.remove("filename")
#fob.close()
#fob.name fob.mode fob.softspace-->returns Boolem if whitespaces or nee lines are there in a file
#fob.seek(offsetoffile) fob.tell()--->tells how many chars are present
kk={1,23,4,6,7,8,9}
#k.add(77)
#k.__len__()
##k.update([4,5,66,677])
##rint(kk," ",kk.__len__())
#
print(sum(i for i in range(11)))
#-->enumerate() finction(builtin)
lettup=("Grocery","weed","drugs")
exe=enumerate(lettup,10)
print(type(exe))
print(list(exe))
from functools import  reduce
product=reduce(lambda x,y:x*(y**2),[1,2,3,4])
print(product)
def summing(a,b,c,d):
    sum=a**b+c**d
    return sum
print(summing(b=1,a=2,d=2,c=3))
print(__name__)