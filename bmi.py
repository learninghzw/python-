#!/usr/bin/env python3
# -*- coding: utf -8 -*-

a=float(input('请输入你的身高(M)：'))
b=float(input('请输入你的体重(KG)：'))
bmi=b/(a*a)
bmi=float('%.2f' % bmi)
if int(bmi)<18.5: #bmi小于18.5属于体重过轻
    print('您的BMI指标是：',bmi)
    print('您的身体属于过轻')
elif int(bmi)<25.00:#bmi指数为18.5-25属于正常体重
    print('您的BMI指标是：',bmi)
    print('您的身体指标正常')
elif int(bmi)<28.00:#bmi指数为25-28属于过重
    print('您的BMI指标是：',bmi)
    ptint('您的身体属于过重')	
elif int(bmi)<32.00:#bmi指数为28-32属于肥胖
    print('您的BMI指标是：',bmi)
    print('您的身体属于肥胖')
else:             #bmi指数高于32属于严重肥胖
    print('您的BMI指标是：',bmi)
    print('您的身体属于严重肥胖')