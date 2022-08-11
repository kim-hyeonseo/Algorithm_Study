init_value=int(input())
x=y=0

if init_value<10:
    x=0
    y=init_value
else :
    x=init_value//10
    y=init_value%10
cnt=0

while 1:
    cnt+=1
    
    tmp=x
    x=y
    y=(tmp+y)%10
    if (10*x+y)==init_value:
        break

print(cnt)

