dia_dic={
    2 : 'ABC', 3 : 'DEF', 4 : 'GHI', 
    5 : 'JKL', 6 : 'MNO', 7 : 'PQRS', 
    8 : 'TUV', 9 : 'WXYZ'
    }

input_string=input()
return_list=[]
for key in input_string:
    for i in range(2,10):
        if key in dia_dic[i]:
            return_list.append(i)

print(sum(return_list)+len(return_list))

# 9 2+(9-1) =10
# 2 2+(2-1) =3
# 9+2+n  13