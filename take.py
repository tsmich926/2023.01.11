import requests
url = ('https://jsonplaceholder.typicode.com/posts')
r= requests.get(url).json()
f_d = r[0]
# print(f_d)
# print(f_d.get('title'))
# l=len(r)
# print(l)
for i in range(10):
    print(r[i].get('title'))



