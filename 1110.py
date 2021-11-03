import sys
N = int(sys.stdin.readline())
count = 0

while True:
    a = N//10
    b = N%10
    sum=a+b
    sum%10
    
    if (b*10+(sum%10)):
        count+=1
    else:
        count+=1
        
    print(count)
    break
dL =0 
