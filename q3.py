n = int(input("Enter length of input set: "))
l = []
for _ in range(n):
    i = input(f"Input {_ + 1}: ")
    l.append(i)

b = []
output = []
length = len(str(bin(pow(2,n)).replace("0b","")))

for j in range(pow(2,n)):
    binary = bin(j).replace("0b", "")
    c = ("0"*(length - len(str(binary)) - 1) + str(binary))
    b.append(c)

for q in b:
    e = []
    for w in range(n):
        if int(q[w]) == 1:
            e.append(l[w])
    output.append(e)

print(output)