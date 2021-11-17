import sys
N = int(sys.stdin.readline())
list_ox = list(str(sys.stdin.readline().strip()) for i in range(N))

for i in list_ox:
    final_sum = 0
    sum = 0
    for com_i in i:
        if com_i =='O':
            sum +=1
        else:
            sum = 0
        final_sum +=sum
    print(final_sum)
