import math



N,M=map(int,input().split())


save=list(map(int,input().split()))

result=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if(save[i]+save[j]+save[k]>M):
        continue
      else:
        result=max(result,save[i]+save[j]+save[k])


print(result)    



