import sys
list_num = list(int(sys.stdin.readline().strip()) for i in range(3))
sum = list_num[0] * list_num[1] * list_num[2]
sum_re = str(sum)

for i in range(0,10):
    i_re = str(i)
    cnt = sum_re.count(i_re)
    print(cnt)