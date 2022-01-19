
def experssion(n):
    f = n[1] - n[0] - 1
    for i in range(1, len(n)):
        if f < n[i] - n[i - 1]:
            f = n[i] - n[i - 1]
        else:
            return False
    return True

b = list(map(int,input().split( )))
experssion(b)


