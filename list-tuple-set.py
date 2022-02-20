# list - [], maintains order, can be modified, can have duplicates
# tuple - (), maintain order, cannot be modified, can have duplicates
# set - {}, order is not guranteed, cannot have duplicates, can be modified


#list and tuple can ce accessed using sub script notation
#subscript notation doesnot make any sense in sets as there is no order maintain, and hence it not work with sets

l = ["a", "b", "c"]
t = ("a", "b", "c")
s = {"a", "b", "c"}

print(l)
print(l[1]) # subscript notation

l[0] = "x"
l.append(2)
l.remove("b")
print(l)

s.add(2)
s.add("a")
s.remove("c")
print(s)

s1 = {1,2,3}
s2 = {2,3,4}

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.union(s2))
print(s1.intersection(s2))


#lists comparision
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2)