user_string = input('Please enter a long string : ').split(" ")
new_string = user_string[::-1]
new_string = " ".join(new_string)
print(new_string)