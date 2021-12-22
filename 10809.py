#10809_find_alphabet

import sys
import string

s = sys.stdin.readline()

for j in string.ascii_lowercase:
    cnt = 0
    if j in s:
        for i in s:
            if i != j:
                cnt += 1
            else:
                print(cnt,end=" ")
                break
    else:
        print(-1,end=" ")
            



