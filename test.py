hi = 'hi'
hi2 = hi
print(hi,hi2)

a = 58
b = '58'
print(a+1,b+'1')

c = 300 >200
print(c)

print(hi == 'hi')
print(hi2 == 'hi2')

d={}
s=['a','b','c','d']
for c in s:
    if c in d.keys():
        d[c]+=1
    else:
        d[c]=1
print(d)

a=4
s[a//2]