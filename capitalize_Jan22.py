'''Task 2 You are asked to ensure that the first and last names of people
 begin with a capital letter in their passports. For example, alison heck 
 should be capitalised correctly as Alison Heck.
'''
import string 
s="geetha sri"
l=s.split(" ")
s=''
for i in l:
     s=s+i.capitalize()+' '
print(s)
        
       

        