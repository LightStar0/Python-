#-*- ciding : utf-8 -*-

a=int(input("請輸入起始值"));
b=int(input("請輸入終值"));
字串="";
for 外 in range(2,10):
    for 內 in range(2,10):
        字串+="%2d*%2d=%3d"%(a*b);
        print(字串);
