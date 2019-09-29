class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def getArea(self):
        return  self.l*self.b
class Square(Rectangle):
    def __init__(self,sid):
        self.sid=sid
        Rectangle.__init__(self,sid,sid)
    def getArea(self):
        return self.sid*self.sid
sq=Square(4)
re=Rectangle(4,5)
print(sq.getArea())
print(re.getArea())
#import sys
#print(sys.argv)
#print(sys.winver)
#sys.exit()
import  os
print(os.name)
print(os.getcwd())
import  datetime as d
print(d.MAXYEAR)
print(d.MINYEAR)
print(d.datetime.today())
print(d.timezone)
import re
print(re.sub('abc','*','abcdefg hijkabc'))
print(re.sub('[ab]','@','abcdefg hijkabc'))
print(re.sub('[abc][123]','$','a1+b2+d3'))
my_list=[1,2,3,4,5]
def squaring(my_list):
    for i in my_list:
        yield i*i
result=list(squaring(my_list))
print(result)