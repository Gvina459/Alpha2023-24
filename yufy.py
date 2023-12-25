import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import pandas as pd

img1 = cv2.imread(r"C:\Users\nirim\Desktop\Python Projcets\imae3.jpg")

gray1 = np.array(cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY))
gray1=gray1[0:457, 0:430]

Arr1=[]

Arr2=[]

for c in range(-10, 10, 1):

    ls=[]
    y=int(img1.shape[0]*0.5)
    sum=0
    ls3=[]
    ls2=[]
    
    ls=gray1[y]

    for i in ls:
        sum=sum+i

    for i in range(len(ls)):
        ls3.append(ls[i]/sum)

    #40pixels == 0.5cm
    #4cm between rod and screen = 320pixels

    for i in range(len(ls), 0 , -1):
        ls2.append(math.atan(i/320))
    
    if c==0:
        for i in range(len(ls)):
            Arr1.append(ls2[i])

        for i in range(len(ls)):
            Arr2.append(ls3[i])
    else: 
        for i in range(len(Arr1)):
            Arr1[i]=Arr1[i]+ls2[i]

        for i in range(len(Arr2)):
            Arr2[i]=Arr2[i]+ls3[i]

for i in range(len(Arr1)):
    Arr1[i]=Arr1[i]/10

for i in range(len(Arr2)):
    Arr2[i]=Arr2[i]/10

print(gray1[y])

#plt.hist2d(Arr1 ,Arr2, density=False, bins=len(Arr1))
plt.plot(Arr1, Arr2, 'k.')
plt.show()

#df = pd.DataFrame(Arr1,Arr2)
#df.to_excel('AnglesDist.xlsx', sheet_name='AnglesDist')