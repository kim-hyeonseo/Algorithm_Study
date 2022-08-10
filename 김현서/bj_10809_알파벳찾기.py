

input_string=input()
ref_list=[[str(-1),0] for _ in range(26)]

for i in range(26):
    ref_list[i][1]=chr(i+97)

print(ref_list)

result_list=[str(-1)]*26
for i in range(len(input_string)):
    for j in range(len(ref_list)):
        if input_string[i]== ref_list[j][1]:
            if result_list[j]!=str(-1):
                pass
            else:
                 result_list[j]=str(i)

print(' '.join((result_list)))
