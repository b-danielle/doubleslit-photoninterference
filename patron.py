import math
from math import sqrt
import numpy as np
import cmath
from cmath import exp



probabilidad=open('probabilidad.txt','w')
probabilidadx=open('probx.txt','w')



r0=.1e-4 
lambda1=810e-9
pi=3.1415926 
k=(2*pi)/lambda1 
hb=1.054e-34 
epsilon=8.85e-12  
v=3e8 
omega=(v*2*pi)/lambda1 
E=hb*omega 
pz=.5  
R=.5  
lx=.6
ly=.6 
im=1j 


n=350
t=2*n+1 


x1=r0/2  
x2=-r0/2 
z=0     
y=0     



for i in range(t):
   
    px=-lx + i*(lx/n)  
    
    for m in range(t):
       
       py=-ly + m*(ly/n)   
       d2=sqrt((px-x1)**2+(py-y)**2+(pz-z)**2)   
       d1=sqrt((px-x2)**2+(py-y)**2+(pz-z)**2) 
       phi= k*(d1-d2)               
       d=(d1+d2)/2    #
       q=im*sqrt((E)/(2*epsilon*4*pi*R))/d      
       p=(q*(q.conjugate()))                        
       PA=p*(1 + math.cos(phi))  
       prob=PA.real
       probabilidad.write(' {0:5.4f} {1:5.4f} {2:5.13f} \n'.format(px,py,prob))  

  


m=6000
lx=1

for i in range(2*m+1):
    
       px=-lx + i*(lx/(m))   
       d2=sqrt((px-x1)**2+(0-y)**2+(pz-z)**2)  
       d1=sqrt((px-x2)**2+(0-y)**2+(pz-z)**2) 
       phi= k*(d1-d2)  
       d=(d1+d2)/2                  
       q=im*sqrt((E)/(2*epsilon*4*pi*R))/d      
       p=(q*(q.conjugate()))                         
       PA=p*(1 + math.cos(phi))   
       probx=PA.real 
       probabilidadx.write('{0:5.6f} {0:5.13f}  \n'.format(px,probx))
   

    
     
probabilidad.close() 
probabilidadx.close()



























        
        
    
