'''Task 2
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

'''

#solution 1

n=35
if n%2!=0 or (6<=n<=20 and n%2==0):
    print("Weird")
else:
    print("Not Weird")

#solution 2
if n%2!=0:
    print("Weird")
elif (6<=n<=20 and n%2==0):
   print("Weird")
else:
   print("Not Weird")


