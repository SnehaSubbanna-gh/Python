def threesum(A):
    i =0
    x=0
    y=0
    z = 0
    B = []
    if len(A)<3:
        return (A)
    else:
        for num in A:
            x = A[i]
            y = A[i + 1]
            if num-(x+y) == 0:
                B.append(x)
                B.append(y)
                B.append(num)
                i+=1
        return (B)

A = [1,2,-3]
print(threesum(A))