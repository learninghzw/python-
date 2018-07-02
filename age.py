# -*- coding: utf-8 -*-

age=input('请输入你的年龄：')
if int(age)>=18:    #大于18岁成年了
    print('你的年龄是：',age)
    print('恭喜你成年了')
elif int(age)>=12:  #还属于青少年
    print('你的年龄是：',age)
    print('你是个青少年')
else:          #年龄太小
    print('你的年龄是：',age)
    print('你还是个娃')