def get_sum(a,b):
    #good luck!
    sum = 0
    if a == b:
        return 1
    else:
        for i in range(a, b+1):
            sum += (a + i)
            i = i + 1
    return sum


print get_sum(0,5)