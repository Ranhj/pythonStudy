# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/3 16:09
# IDE:        PyCharm
# className:  qiePianDemo.py
str1 = '0123456789'
print(str1)
print(str1[0])
print(str1[0:4])    # 0123  结束位置不包含下标数值
print(str1[0:4:1])  # 0123  默认步长为1，平时省略不写
print(str1[0:4:2])  # 02    步长为2，间隔一个下标取值
print(str1[:5])     # 01234 开始位置省略不写，默认从下标0开始取值
print(str1[:5:2])   # 024 开始位置省略不写，默认从下标0开始取值，下标为2，间隔一个下标取值
print(str1[:9:3])   # 036 开始位置省略不写，默认从下标0开始取值，下标为3，间隔两个下标取值
print(str1[3:])     # 3456789   结束位置不写，默认从开始位置取值到最后
print(str1[3::2])   # 3579   结束位置不写，默认从开始位置取值到最后，步长为2，间隔一个下标取值
print(str1[:])      # 0123456789    开始结束位置都不写，默认取全部
print(str1[::])     # 0123456789    开始结束位置步长都不写，默认取全部
print(str1[::2])    # 02468         开始结束位置都不写，步长为2，默认从第一个下标间隔两个下标取值到最后下标
# 负数测试
print('-----------负数-----------')
print(str1[::-1])   # 9876543210    开始和结束位置都不写，步长为-1时，默认从最后一个下标往第一个下标取值，倒着取值！
print(str1[::-2])   # 97531    开始和结束位置都不写，步长为-2时，默认从最后一个下标往第一个下标间隔2个下标取值，倒着取值！
print(str1[-9:-1])  # 12345678  下标-1表示最后一个数据，依次向前类推
# 终极测试
print(str1[-4:-1:1])    # 678
print(str1[-4:-1:-1])   # 不能选取出数据：从-4开始到-1结束，选取方向从左到右，但是-1步长是从右向左取
print(str1[-1:-4:-1])   # 987
