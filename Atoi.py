def atoi(a):
    s = a.split()
    n = []
    if a[0].isalpha():
        return 0
    else:
        for word in a.split():
            if "-" in word:
                n.append(word)
            elif word.isdigit():
                n.append(word)
            elif word.isdecimal():
                n.append(word)
            string_ret = [str(num) for num in n]
            ret_string = "".join(string_ret)
        if "-" in string_ret:
            intret = ret_string * -1
        elif word.isdecimal():
            float_str = float(ret_string)
            intret = int(float_str)
        else:
            intret = int(ret_string)

        if intret > ((-2) ** 31) and intret < (2 ** 31):
            return intret
        elif intret < 0 and intret <= (2 ** 31):
            return ((-2) ** 31)
        else:
            return ((2 ** 31) - 1)


a = "3.14159"
print(atoi(a))
