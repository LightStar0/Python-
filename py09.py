'''
# -*- coding: utf-8 -*-

n = int(input('0~不超過多少:')) # 輸入  
for i in range(n):
    print(i)
    
a = int(input('從多少:')) 
b = int(input('到多少:')) 
for i in range(a,b+1):
    print(i)

step = int(input('間隔:'))     
for i in range(a,b+1,step):
    print(i)   '''

a=int(input("起始"));
b=int(input("終值"));
for i in range(a,b+1):
    print(i)

for q in range(a,b+1,5):
    print(q);
    
    
