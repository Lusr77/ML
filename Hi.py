# import  sys
 # from  math import  factorial
 # print(len(sys.argv))
 # print(sys.argv)
 # print(factorial(int(sys.argv[1])))
 # print(int(sys.argv[2])+int(sys.argv[3]))
 # print("\n")
def message():
    '''
    THis python function returns
    a message displaying that
    waht is to be done
    '''
    print("Hrllo PYHTON")
#call fun
message()
#kk=[13]
# for i in kk:
  #  for j in range(2,i):
   #     print(j)
#a,b,c=eval(input()),eval(input()),eval(input())
#if(a>b>c):
 #   print(a,"is greater")
a=10
x=bin(a)
z=~a
print(bin(z))
x,y=120,100
print(x & y)
print(x | y)
import  math as mt
x=mt.gcd(23,45)
print(x)
import  sympy as st
#for i in range(1,21):
#    flag=0
#    for j in range(2,i):
#        if(i%j==0):
#            flag=1;
 #           break;
 #   if(flag==0):
  #      print(i,'is a prime')
for i in range(1,5):
     if(st.isprime(i)):
         print(i)
print("first n primes",st.prime(6))

