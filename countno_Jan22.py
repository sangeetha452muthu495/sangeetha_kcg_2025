'''Task 2
Given an integer N, write a program to count the number of digits in N.45678
'''


n=int(input())
count=0
while(n!=0):
    n=n//10
    count+=1
print(count)
    