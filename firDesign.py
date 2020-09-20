"""
Created on Sun Mar  1 18:16:41 2020

@ Name: Abhishek Dhital
  ID:   1001548204
"""

import numpy as np
import matplotlib.pyplot as plt


file=open("data-filtering.csv")
d=np.genfromtxt(file,delimiter=",")
data=np.array(d)


fs=2000
fc1,fc2=50,280   #cutoff frequencies for low pass and high pass filter respectively
L=21      #filter length
M=L-1
n=0
w1=[]    #w1 and w2 are the filter weights for 
w2=[]    #low pass and high pass filters respectively

while (n<L):
    if (n==M/2):
        w1.append(2*fc1/fs)
        w2.append(1-2*(fc2/fs))
    else:
        w1.append((np.sin(2*np.pi*fc1/fs*(n-M/2)))/(np.pi*(n-M/2)))
        w2.append(-(np.sin(2*np.pi*fc2/fs*(n-M/2)))/(np.pi*(n-M/2)))        
    n+=1

hpf=np.convolve(data,w2) #high pass filter applied to the original signal
lpf=np.convolve(data,w1) #low pass filter applied to the original signal
print(hpf.shape)
t=np.arange(0,2000,1)  #creation of the time axis 

figure1=plt.figure()
figure2=plt.figure()

plt1=figure1.add_subplot(611) #original signal
plt2=figure1.add_subplot(613) #4Hz signal
plt3=figure1.add_subplot(615) #after application of lowpass filter

plt4=figure2.add_subplot(611) #original signal
plt5=figure2.add_subplot(613) #330Hz signal
plt6=figure2.add_subplot(615) #after application of high pass filter

plt1.plot(t,data)
plt1.set_title("original signal")

fourHz=np.cos(2*np.pi*4*t/fs)
plt2.plot(t,fourHz)
plt2.set_title("4 Hz signal")

t2=np.arange(0,lpf.size,1)  #after convolution the signal has more than 2000 values
plt3.plot(t2,lpf)
plt3.set_title("application of lowpass filter")

t3=np.arange(0,100,1) #in order to plot only the first 100 values of the signals
plt4.plot(t3,data[:100])
plt4.set_title("original signal")

tHz=np.cos(2*np.pi*330*t3/fs)
plt5.plot(t3,tHz[:100])
plt5.set_title("330 Hz Signal")

plt6.plot(t3,hpf[:100])
plt6.set_title("application of highpass filter")


plt.show()
file.close()

    
    
    
    
    
    


    
    
    
