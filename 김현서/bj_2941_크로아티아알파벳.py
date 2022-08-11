ref_list=['dz=','c=','-c','d-','lj','nj','s=','z=']

input_string=list(input())

cnt=0
for i in range(0,len(input_string)):
    try :
        # dz= 먼저 검토 후 str 0 으로 치환
        if f'{input_string[i-1]}{input_string[i]}{input_string[i+1]}' in ref_list:
            input_string[i-1]=input_string[i]=input_string[i+1]='0'
            cnt+=1
        # 나머지 검토 후 str 0으로 치환
        elif f'{input_string[i]}{input_string[i+1]}' in ref_list:
            input_string[i]=input_string[i+1]='0'
            cnt+=1
        # ref_list 의 경우 그대로
        else:
            pass
        #i+1, i+2 때문에 i
    except IndexError:
        break

# print(input_string)
 
for j in input_string:
    if j.isalpha():
        cnt+=1

print(cnt)