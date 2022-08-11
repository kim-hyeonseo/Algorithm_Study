al_string='abcdefghijklmnopqrstuvwxyz'

input_string=input()
result_list=['-1']*26
for alp in al_string:
    for char in input_string:
        if alp == char:
            result_list[al_string.index(alp)]=f'{input_string.index(char)}'
            
print(result_list)
print(" ".join(result_list))


