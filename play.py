# import random
# s = range(5)
# for i in range(1,5):
#     print(i)


# s = range(1,10)
# #r = random.choice(s)
# random.sample(s, 3)
# print(r)


# import random
# s = range(1,46)
# print(s)
# r= random.sample(s,6)
# m = sorted(r)
# print("행운의 번호는 ",m)
# \

import requests 
url='https://api.agify.io/?name=michael'
r= requests.get(url)
print('r===>',r)
r1 = r.json()
print('r1====>',r1)
# requests.get('url').json()
response = requests.get(url).json()
name = r1.get('name')
age = r1.get('age')
print(name,'의 평균나이는',age,'입니다')
print(f'{name}의 평균나이는 {age}입니다.')