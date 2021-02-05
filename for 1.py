# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:30:57 2021

@author: DELL
"""

#lista=["R1" , ' R2 ' , ' R3 ' , ' R4 ' , ' R5 ']
#for i in lista:
    #print(i,end= '' )
listasw=[]
listaR=[]
listaD=[]
lista=["R1" , ' R2 ' , ' R3 ' , 
       ' S1 ' , ' S2 ' , ' S3 ' , 
       '  R4 ' , ' R5 ', 'PC',
       ' Ps5']

for i in lista:
    if 'S' in i:
        listasw.append(i)  
       # print(i,end= ' ')
    elif "R" in i:
        listaR.append(i) 
    else:
        listaD.append(i)

        print('Sw: ',listasw,'\nR:',listaR,'\nD:',listaD)
 
        