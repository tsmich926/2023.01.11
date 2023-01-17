import requests
import random
number= random.randint(1,1050)
print(f'{number}회 로또 번호 출력')
url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={number}'

r = requests.get(url)
r1 = r.json()
response = requests.get(url).json()

number1 = r1.get('drwtNo1')
number2 = r1.get('drwtNo2')
number3 = r1.get('drwtNo3')
number4 = r1.get('drwtNo4')
number5 = r1.get('drwtNo5')
number6 = r1.get('drwtNo6')
number7 = r1.get('drwtNo7')


# for i in range(1,6):
#     print(f'{i}출력')

for i in range(1,7):
    key = f'drwtNo{i}'
    print(response.get(key))

# r= str(1) #숫자를 문자로
# r = int('1') #정수형으로