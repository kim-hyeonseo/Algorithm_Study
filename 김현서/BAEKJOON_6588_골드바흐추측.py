prime_number_list=[3]
n=int(input())


# 홀수 소수 만들기
for j in range(3,n,2):
    detect=0
    for i in range(len(prime_number_list)):
        if j%prime_number_list[i]==0:
            detect=0
            break
        else : 
            if j in prime_number_list:
                detect=0
            else : 
                detect=1
    if detect==1:
        prime_number_list.append(j)

# 조건 거르기
result_pair=[]
for i in range(len(prime_number_list)):
    for j in range(len(prime_number_list)):
        if prime_number_list[i]+prime_number_list[j]==n:
            result_pair.append((prime_number_list[i],prime_number_list[j]))

#쌍 구하기
result_sub=[]
value_sub=0
value_sub_idx=0
for i in range(len(result_pair)):
    ref_value=0
    if result_pair[i][0]>result_pair[i][1]:
        # result_sub.append(result_pair[i][0]-result_pair[i][1])
        ref_value = result_pair[i][0]-result_pair[i][1]
    else :
        # result_sub.append(result_pair[i][1]-result_pair[i][0])
        ref_value = result_pair[i][1]-result_pair[i][0]
    if value_sub<ref_value:
        value_sub = ref_value
        value_sub_idx=i

print(f'{n} = {result_pair[value_sub_idx][0]} + {result_pair[value_sub_idx][1]}')