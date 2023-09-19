str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

l,m = [],[]
check = 0

for i in range(len(str1)):
    if str1[i] != " ":
        l.append(str1[i].lower())

for j in range(len(str2)):
    if str2[j] != " ":
        m.append(str2[j].lower())

for x in range(len(l)):
    for y in range(len(m)):
        if l[x] == m[y]:
            check += 1
            m[y] = []
            l[x] = []


if check == len(l):
    print("BALANCED")
else:
    print("UNBALANCED")
