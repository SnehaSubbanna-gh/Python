def rev(b):
    y = 0;
    x = abs(b)

    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    if b>0 and y < (2 ** 31):
        return y
    elif b<0 and y <= (2 ** 31):
        return y * -1
    else:
        return 0


a = 1534236469
print (rev(a))
