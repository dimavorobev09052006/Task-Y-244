import random
a = [random.randint(-20, 20) for i in range(10)]
b = []
c = []
print(a)
print(min(a))
print(a.index(min(a)))
for i in range(len(a)):
    if a[i] >= 0:
        b.append(a[i])
print(b)
c = list(set(a)-set(b))
print(c)
