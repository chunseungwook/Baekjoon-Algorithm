import sys
list_nums = list(int(sys.stdin.readline().strip()) for i in range(10))
list2_num=[]
cnt = 0

for list_num in list_nums:
    list2_num.append(list_num%42)
    
set_num = set(list2_num)
re_list2_num = list(set_num)
len_list2_num = len(re_list2_num)
print(len_list2_num)