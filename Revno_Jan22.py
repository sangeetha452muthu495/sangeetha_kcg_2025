
'''Task 1
Given a number N reverse the number and print it'''

#solution 1:
N=int(input())
res=0
while(N!=0):
    rem=N%10
    res=res*10+rem
    N=N//10
print(res)