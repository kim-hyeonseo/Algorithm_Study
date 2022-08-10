import math
a,b,c=map(int,input().split())

# a+b*n<c*n
if c==b: # zerodivision
    print(-1)

elif a/(c-b)<0:
    print(-1)

else :
        if a%(c-b)==0:
            n=int(a/(c-b)+1)
            print(n)

            # n 이 자연수인 경우 1 만큼 적게 출력되기 때문에 +1
        else :
            n=int(math.ceil(a/(c-b)))

            # n 이 자연수가 아닌 경우 올림
            print(n)
