'''
# -*- coding: utf-8 -*-
a = int(input('請輸入成績:')) # 輸入  
if 0<=a<=100:
    print('成績:%d'%a)
else:
    print('錯誤!')'''

a=int(input("請輸入成績"));
if 0<=a<=100:
    if(a>=90):
        print('成績:',a,'A級分');
    elif(a>=80):
        print('成績:',a,'B級分');
    elif(a>=70):
        print('成績:',a,'C級分');
    elif(a>=60):
        print('成績:',a,'D級分');
    else:
        print("不及格!!");
else:
    print("輸入錯誤")
