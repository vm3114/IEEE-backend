t = int(input("Enter number of test cases: "))

for i in range(t):
    n = int(input("Enter size of array: "))
    array = [""]*n

    for _ in range(n):
        j = int(input("Enter integer: "))
        array[_] = j

    add,sub,sum = [],[],0
    k = 0
    while k <= n-1:
        add.append(abs(array[k]))
        if k != n-1:
            sub.append(abs(array[k+1]))
        k = k + 2

    add.sort()
    sub.sort(reverse = True)

    m = add[0]
    add[0] = sub[0]
    sub[0] = m

    for x in add:
        sum = sum + x
    for y in sub:
        sum = sum - y

    print(sum)