import sys
N = int(sys.stdin.readline())
num = N
count = 0

while True:
    a = num //10
    b = num % 10
    sum=a+b
    sum_b = sum%10
    num = (b*10+(sum_b))
    count+=1
    if (num == N):
        break    
print(count)
