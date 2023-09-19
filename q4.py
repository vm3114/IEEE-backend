l = []
for _ in range(5):
    i = int(input(f"Enter number {_ + 1}: "))
    l.append(i)

l.sort()
m = []

for j in range(4):
    p, q = l[j],l[0]
    while q != 0:
        p, q = q, p%q
    m.append(p)

m.sort()
print(f"The GCD is: {m[0]}")