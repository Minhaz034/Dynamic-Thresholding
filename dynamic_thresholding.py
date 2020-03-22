#minhaz bin farukee 1503034 created:17/2/2020
#update:23/3/2020
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

def mean(Arr,start,end,size):
    g=0
    mean=0
    sum=0
    for g in range(start,end+1):
        sum+=Arr[g]
    mean=sum/size
    return mean   

def variance(Arr,start,end,size):
    h=0
    sigma=0
    square=0
    for h in range(start,end+1):
        square+=Arr[h]*Arr[h]
    mew=mean(Arr,start,end,size)
    sigma=(square/(size-1))-((size*mew**2)/(size-1))   
    return sigma
#def packet_at(time,dataset):
dataset=pd.read_csv("test_data.csv")

'''
num_packet=dataset.No
time=dataset.Time
source=dataset.Source
destination=dataset.Destination
protocol=dataset.Protocol
'''
#converting to list
i=0
x=0
k=0
rows=700
cols=700
p=len(dataset)

A1=[]
source_ip=[]
for row in range(rows):
    source_ip += [[0]*cols]
    
destination_ip=[]
for row in range(rows):
    destination_ip += [[0]*cols]

protocol=[]
for row in range(rows):
    protocol += [[0]*cols]

current_time=0   
test=[]
k=0
counter=0

max_time=dataset['Time'].max()
#aggregation of packet features:
while current_time<=max_time:
    x=0
    k=0
    #print(counter,i)
    counter+=1
    
    while dataset.iat[i,1]>=current_time and dataset.iat[i,1]<current_time+1: 
        
        x=x+1        
        #source_ip.append(dataset.iat[i,2])
        source_ip[current_time][k]=dataset.iat[i,2]
        destination_ip[current_time][k]=dataset.iat[i,3]
        protocol[current_time][k]=dataset.iat[i,4] 
        k+=1
        i=i+1
        if i>=p:
            break        
    A1.append(x)        
    current_time+=1
    test.append(current_time)

#no of elements calculation
t=0
usip=[]
udip=[]
uprotocol=[]
for t in range(int(max_time)+1):    
    usip.append(len(Counter(source_ip[t]))-1)
    udip.append(len(Counter(destination_ip[t]))-1)
    uprotocol.append(len(Counter(protocol[t]))-1)          



o=variance(A1,0,2,3)
#normalization:
max_x1=max(A1)    
max_usip=max(usip)
max_udip=max(udip)
max_protocol=max(uprotocol)
for s in range(int(max_time)+1):
    A1[s]=A1[s]/max_x1
    usip[s]=usip[s]/max_usip
    udip[s]=udip[s]/max_udip
    uprotocol[s]=uprotocol[s]/max_protocol

'''
#plot:
plt.bar(test, usip, align='center', alpha=0.5)
plt.show()
plt.bar(test, udip, align='center', alpha=0.5)
plt.show()
plt.bar(test, uprotocol, align='center', alpha=0.5)  
plt.show()
'''      





#Dynamic thresolding:
N1=0
window_size=11
beta=1.5
end=len(A1)
i=0
mew=[]
sigma=[]
threshold=[]
for i in range(end-window_size):
    mew.append(mean(usip,i,i+window_size,window_size))
    sigma.append(variance(usip,i,i+window_size,window_size))
    
    threshold.append((mew[i]+sigma[i])*beta) 
    if A1[i]>threshold[i]:
        N1+=1
        
        
        
        
    
    


    