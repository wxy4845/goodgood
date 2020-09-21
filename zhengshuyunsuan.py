# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:28:46 2020

@author: 小别致
"""

import random
#四则运算
from fractions import Fraction
def f(f):#分数的转换
    a=f.numerator #分子
    b=f.denominator #分母
    if a%b==0:#为整数
        return '%d'%(a/b)
    elif a<b:#为真分数
        return '%d%s%d' % (a,'/',b)
    else:#为带分数
        c=int(a/b)
        a = a - c * b
        return '%d%s%d%s%d' % (c,'’',a,'/',b)
def ysfz():
    sym = ['＋', '－', '×', '÷']
    f= random.randint(0, 3)
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    result = 0
    if f== 0:#加法
       result  = n1 + n2
    elif f == 1:#减法，要先比较大小，防止输出负数
        n1, n2 = max(n1, n2), min(n1, n2)
        result  = n1 - n2
    elif f== 2:#乘法
        result  = n1 * n2
    elif f == 3:#除法，要比较大小
       
        result =Fraction(n1, n2)
    print(n1, sym[f], n2, '= ', end='')

    return result
print('请输入1进行四则运算') 
n=int(input())
#当输入1时，进行四则运算，调用函数syzs()
if n==1:
    while True:
        result  = ysfz()
        j= input()
       
        if j== f(result ):
            print('well',f(result))
        else:
            print('more again,the answer is', f(result))