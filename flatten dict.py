def let(k):
    list = []
    i =0
    while i < len(k):
        count = 1
        while i+1 < len(k) and k[i+1]:
            i+=1
            count += 1
        list.append(str(count)+k[i])
        i +=1
    return ''.join(list)
z=1
n = int(input())
for i in range(n):
    print(z)
    z=let(str(z))