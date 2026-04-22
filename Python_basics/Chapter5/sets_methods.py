
s = {1,2,3,4, 5, 2, 3,4,5, "Sam"}
print(s)

#print(type(s))

#add() method
s.add(100)
print(s)

#update()
t = {1, 2}
t.update([2,3,4,5])
print(t)

#remove : gives error if element not found
t.remove(4)  
print(t)

#discart() : no error if not found
t.discard(7)
print(t)


#pop() : removes random element
t.pop()
print(t)


#clear() : removes everything
# t.clear()
# print(t)

#union()
a = {1,2}
b = {3,4}

print(a.union(b))

#intersection()
c={1,2,3,4,5}
d={3,4,5,6,7}
print(c.intersection(d))

#difference() : element in 1st bt not in 2nd
e = {1,2,3,4,5,6,7}
f = {5,6,7,8,9,10}
print(e.difference(f))



