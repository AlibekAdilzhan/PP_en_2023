n = int(input())

d = n % 10
c = (n // 10) % 10
b = (n // 100) % 10
a = n // 1000

print((a - d)**2 + (b - c)**2 + 1)