# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:59:42 2018

@author: SONU
"""
import math as ma
import numpy as np
from scipy.io import wavfile
from scipy import signal 

rate,audData = wavfile.read("abc.wav")

print ("Length of wav file(in s) = " + str(audData.shape[0]/rate))
print ("rate =" + str(rate))
print (audData.shape)

rate1,echo = wavfile.read("ir_greekhall.wav")


print(echo.shape)
print(rate1)
print(np.argmax(audData[:,0]))
print(np.argmax(audData[:,1]))

aud = audData[:,0]
ch = echo[:,0]

eq = 0
for it in range(len(ch)):
    eq = eq + ch[it]**2

eq = eq/len(ch)
eq = np.sqrt(eq)
ch = ch/eq

"""
x0 = np.zeros(8050)
x1 = np.zeros(8050)

x0[0] = 1
x1[0] = 1

x0[4000] = 0.9
x1[4000] = 0.9

x0[6000] = 0.8
x1[6000] = 0.8


x0[8000] = 0.6
x1[8000] = 0.6

for i in range(4000) :
    x0[i]=np.exp(-i/2.0)
    x1[i]=np.exp(-i/2.0)
"""

y = np.convolve(aud,ch)
#y1 = np.convolve(audData[:,1],ch2)

#combined = np.vstack((y0,y1)).T
combined = y
combined = np.asarray(combined , dtype=np.int16)


wavfile.write("YO.wav",rate,combined)