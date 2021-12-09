import sys
num = int(sys.stdin.readline())

hansu = 0
for i in range(1,num+1):
    list_num = list(map(int,str(i)))
    if i<100:
        hansu += 1
    elif list_num[1] - list_num[0] == list_num[2] - list_num[1]:
        hansu += 1
print(hansu)

