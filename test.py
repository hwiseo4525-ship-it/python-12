# 32
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a|b
d = a & b
print(c, d)

# 33
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a - b
d = a ^ b
print(c, d)

# 34
a = {1,2,3,4,5}
a.update({100})
print(a)

# 35
a = {100, 200, 300, 400, 500}

a.intersection_update({400, 500, 600, 700, 800})
print(a)

a = {100, 200, 300, 400, 500}
a.difference_update({400, 500, 600, 700, 800})
print(a)

a = {100, 200, 300, 400, 500}
a.symmetric_difference_update({400, 500, 600, 700, 800})
print(a)

# 36
a = {100, 200, 300, 400, 500}
b = {400, 500, 600, 700, 800}
if a.issuperset(b) and a.issubset(b):
    print("동시")
elif a.issuperset(b):
    print("상위")
elif a.issubset(b):
    print("부분")
else:
    print("해당 없음")

# 37
a = {1,2,3,4,5}
a.add(1000)
a.pop()
print(a)

# 38
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
print(multiples)