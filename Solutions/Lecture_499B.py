n=input().split()
n,m=int(n[0]),int(n[1])
my_dict={}
for i in range(m):
    a=input().split()
    a,b=a[0],a[1]
    my_dict[a]=b
lecture=input()
ans=''
for i in lecture.split():
    if i == len(lecture.split())-1:
        if len(i) <= len(my_dict[i]): ans+=i
        else: ans+=my_dict[i]
    else:
        if len(i) <= len(my_dict[i]): ans+=i + ' '
        else: ans+=my_dict[i]+' '
        #9952402150
print(ans)
