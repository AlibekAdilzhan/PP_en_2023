a = int(input())
b = int(input())

# x = 87139461 
# d = 1

# 5 = 101
# 6 = 110
# x = 1111111...11 = 2**31 + 2**30 + 2**29 + ... + 2**0 = 2**32 - 1
# 

for i in range(a, b + 1):
    if int(i**0.5)**2 == i:
        print(i)