#minhaz bin farukee 1503034 created:17/2/2020
#update:23/3/2020
#completely running on update: 25/03/2020
import matplotlib.pyplot as plt
import pandas as pd
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

def DynamicThresolding(Arr,window_size):
    N=0
    #start=0
    window_size=11
    beta=1.5
    end=len(Arr)
    i=0
    mew=[]
    sigma=[]    
    mew.append(mean(Arr,0,0+window_size,window_size))
    sigma.append(variance(Arr,0,0+window_size,window_size))
    threshold=(mew[0]+sigma[0])*beta
    for i in range(1,end-window_size):
        #print(mew[i-1])
        mew.append(mean(Arr,i,i+window_size,window_size))
        sigma.append(variance(Arr,i,i+window_size,window_size))
        if mew[i]>2*(mew[i]):
            beta+=0.5 
        else:
            beta-=0.5  
            if beta<1:
                beta=1
        threshold=(mew[i]+sigma[i])*beta
        
        #threshold.append((mew[i]+sigma[i])*beta) 
        if A1[i]>threshold:
            N+=1    
            break
    return N

dataset=pd.read_csv("test_data.csv")

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
A31=[]
A32=[]
A41=[]
A42=[]
uprotocol=[]
for t in range(int(max_time)+1):    
    usip.append(len(Counter(source_ip[t]))-1)
    udip.append(len(Counter(destination_ip[t]))-1)
    uprotocol.append(len(Counter(protocol[t]))-1)          

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

s=0
for s in range(int(max_time)+1):
    A31.append(usip[s]/udip[s])
    A32.append(A1[s]/udip[s])
    A41.append(usip[s]/uprotocol[s])
    A42.append(A1[s]/uprotocol[s])     

#plot:
plt.title('No. of packet vs time:')
plt.xlabel('time(s)')
plt.ylabel('Number of packets')    
plt.bar(test, A1, align='center', alpha=0.5)
plt.show()

plt.title('No. of unique IP vs time:')
plt.xlabel('time(s)')
plt.ylabel('Number of unipue source IP') 
plt.bar(test, usip, align='center', alpha=0.5)
plt.show()

plt.title('No. of unique destination IP vs time:')
plt.xlabel('time(s)')
plt.ylabel('Number of unique destination IP') 
plt.bar(test, udip, align='center', alpha=0.5)
plt.show()

plt.title('No. of Protocol vs time:')
plt.xlabel('time(s)')
plt.ylabel('Number of protocols') 
plt.bar(test, uprotocol, align='center', alpha=0.5)  
plt.show()
      
#Dynamic thresolding:
N1=DynamicThresolding(A1,11)
N2=DynamicThresolding(usip,11)

#DOS attack detection:
N3DOS=DynamicThresolding(A31,11)        
N4DOS=DynamicThresolding(A42,11)  
#print(N3DOS,N4DOS)
if N1>0 and N2>0 and N3DOS>0 and N4DOS>0:
    print("ALERT!!! DOS ATTACK!!! ")
else:
    print("No Dos attack")

#DDOS attack detection:
N3DDOS=DynamicThresolding(A32,11)        
N4DDOS=DynamicThresolding(A41,11)
#print(N3DDOS,N4DDOS)
if N1>0 and N2>0 and N3DDOS>0 and N4DDOS>0:
    print("ALERT!!! DDOS ATTACK!!! ")
else:
    print("No DDos attack")
     
        
        
    
    


    