import sys
C = int(sys.stdin.readline())
Avg_score = 0
AvgOverStd=0

for i in range(C):
   cnt = 0
   list_team = list(map(int,sys.stdin.readline().split()))
   Avg_score = sum(list_team[1:]) / list_team[0]
   for l in list_team[1:]:
      if l >Avg_score:
         cnt +=1
   AvgOverStd = (cnt/list_team[0] * 100)
   #print(AvgOverStd,end = '%')
   print("{:.3f}%".format(AvgOverStd))
