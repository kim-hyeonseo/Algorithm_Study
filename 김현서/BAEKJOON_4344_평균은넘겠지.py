t=int(input())

for i in range(t):
    score_list=[]
    n,*score_list=map(int,input().split())
    cnt=0
    for j in score_list:
        if j>sum(score_list)/len(score_list):
            cnt+=1
    
    print(f'{cnt/n*100:.3f}%')

