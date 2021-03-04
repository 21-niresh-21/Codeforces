n=int(input())
my_dict={}
for i in range(n):
    team=input()
    if n==1:
        print(team)
        exit()
    if team in my_dict:my_dict[team]+=1
    else:my_dict[team]=1
maximum = max(my_dict, key=my_dict.get)  
print(maximum)
