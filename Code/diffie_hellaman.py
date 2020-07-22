
import math
import numpy
print('Enter Public Keys P and G :')
P=int(input('Enter Module (P) :'))
G=int(input('Enter Value of G :'))
a=int(input('Enter Private Key of(Sender) a :'))
b=int(input('Enter Private Key (Receiver) b :'))
x=numpy.mod((math.pow(G,a)),P)
y=numpy.mod((math.pow(G,b)),P)
key_received_alice=y
key_received_bob=x
print('Alice Receive key :',key_received_alice)
print('Bob Receive key :',key_received_bob)

ka = numpy.mod((math.pow(y,a)),P)
kb = numpy.mod((math.pow(x,b)),P)

if(ka==kb):
    print("Secret Key1 :",ka)
    print("Secret Key2 :",kb)
    