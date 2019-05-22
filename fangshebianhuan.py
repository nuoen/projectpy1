#字母对应数字的字典
cton={}
for i in range(26):
    cton[chr(97+i)]=i
#数字对应字母的字典
ntoc=dict(zip(cton.values(),cton.keys()))

c=input('请输入密文')
c=list(c)
#加密
def E(m):
    c=[]
    for mvalue in m:
        each=cton[mvalue]
        each=(each*9+10)
        cvalue=ntoc[each]
        c.append(cvalue)
    return c
#解密
def D(c):
    m=[]
    for cvalue in c:
        each=cton[cvalue]
        each=each-10
        while (each%9!=0 or each<0):
            each=each+26
        each=each/9
        mvalue=ntoc[each]
        m.append(mvalue)
    return m
m=D(c)
print(m)
        
        
    
