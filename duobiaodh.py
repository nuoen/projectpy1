# -*- coding:utf-8 -*-
import numpy as np
#字母对应数字字典
ctondict={}
for each in range(26):
    ctondict[chr(97+each)]=each
#数字对应字母字典
ntocdict=dict(zip(ctondict.values(),ctondict.keys()))
#函数：字符到数字
def cton(chars):
    global ctondict
    nums=[]
    for each in chars:
        nums.append(ctondict[each])
    return nums

#函数：数字到字符
def ntoc(nums):
    global ntocdict
    chars=[]
    for each in nums:
        chars.append(ntocdict[each])
    return chars

A=np.array([[3,13,21,9],[15,10,6,25],[10,17,4,8],[1,23,7,2]])
B=np.array([1,21,8,17]).reshape(4,1)#转置
#解密
def decrypt(C):
    global A
    global B
    An=np.linalg.inv(A)#求逆
    temp1=np.subtract(C-B)#减法
    M=np.mod(np.multiply(An,temp1),26)#乘法，求模
    return M
#加密
def encript(M):
    global A
    global B
    temp2=np.dot(A,M)
    C=np.mod((temp2+B),26)
    return C

ecnum=[]
ecchr=[]
while 1:
    chars=input("请输入")
    chars=list(chars)
    if chars[0]=='#':
        break
    nums=cton(chars)
    M=np.array(nums).reshape(4,1)
    C=encript(M)
    ecnum.extend(C.reshape(1,4)[0].tolist())

ecchr=ntoc(ecnum)
print(ecchr)





