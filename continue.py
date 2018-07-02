# -*- coding:utf -8 -*-

n=0
while n< 10:
    n=n+1
    if n % 2==0:#当n为偶数时，跳过当前循环
        continue 
    print(n)
print('END')
