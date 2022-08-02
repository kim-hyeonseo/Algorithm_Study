node, m=map(int,input().split())

ref_number_list=list(map(int,range(1,node+1)))
output_list=list(map(str,range(1,node+1)))

#쌍 짓기
for iter in range(m):
    arrow, target=map(str,input().split())

    #잇기
    tmp = "".join([target,arrow])
    
    target_index=int(ref_number_list.index(int(target)))
    
    #리스트 생성, 앞에 값이 중복될 경우 리스트 뒷단을 밀고 삽입
    if int(output_list[target_index])>ref_number_list[target_index]:
        output_list.insert(target_index+1, tmp)
        ref_number_list.insert(target_index+1,0)
    else :
        output_list[target_index]=tmp
    
print(ref_number_list)
print(output_list)

#쌍 잇기 - 반복지정
result_list=[]
for i in output_list:
    for j in output_list:
        if int(j)<10:
            break
        if i[-1]==j[0]:
            result_list.append(''.join([i,j[-1]]))

print(result_list)

#가장 긴 수열 뽑기
len_max=0
len_max_value=''
for i in result_list:
    if len(i)>len_max:
        len_max=len(i)
        len_max_value=i

print(len_max, len_max_value)