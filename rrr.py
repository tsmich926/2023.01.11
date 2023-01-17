import random
number= random.randint(1,1050)
print(number)

url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={number}'
print(url)