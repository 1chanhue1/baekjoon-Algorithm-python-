N=int(input())

for i in range(N):
  some=(input())

  check=[]

  flag=0

  for j in range(len(some)):
    if(some[j]=='('):
      check.append(some[j])

    elif(some[j]==')'):
      if(len(check)==0):
        flag=1
        break
      else:
        check.pop(-1)


  if(flag==1 or len(check)!=0):
    print("NO")
  else:
    print("YES")  



 