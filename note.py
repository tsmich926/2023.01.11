#연습장
N = int(input())
num= list(map(int,input().split()))
num.sort()
index = (N+1)//2
print("{}".format(num[index]))
