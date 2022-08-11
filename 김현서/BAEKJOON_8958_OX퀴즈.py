iteration=int(input())

for _ in range(iteration):
    input_string=input()
    total_value=0
    ref_value=0
    for i in range(len(input_string)):
        
        if ord(input_string[i])==79:
            ref_value+=1
            total_value+=ref_value
        elif ord(input_string[i])==88:
            ref_value=0
    print(total_value)

        # 79 88