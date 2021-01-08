def isPalindrome(s):
        string_input = str(s)
        r = string_input[::-1]
        if r == string_input:
            return True
        else:
            return False


s = 122
print(isPalindrome(s))