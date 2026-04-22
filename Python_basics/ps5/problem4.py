#4. What will be the length of following set s: 


s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(s)
print(len(s))

#bcoz the python finds that floting and int values are same as 20 even threr datatypes are different
