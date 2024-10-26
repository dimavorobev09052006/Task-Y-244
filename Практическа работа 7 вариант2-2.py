x = [int(input()) for _ in range(8)]
print(x)
x = [2*a if a<15 else a for a in x] 
print(x)