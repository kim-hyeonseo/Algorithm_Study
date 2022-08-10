
TC= int(input())

for tc in range(1,TC+1):
    n, *input_list=list(map(int,input().split()))


    sum=0
    for i in range(len(input_list)):
        sum+=input_list[i]

    avr=sum/len(input_list)

    cnt=0
    for i in range(len(input_list)):
        if input_list[i]>avr:
            cnt+=1

    print(f'{cnt/len(input_list)*100:.3f}%')
