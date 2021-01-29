num = input('Please enter a number : ')
number = int(num)
if (number % 4) == 0:
    print('The number is divisible by 4')  # print different msg when divisible by 4
elif (number % 2) == 0:
    print('You entered an even number')
else:
    print('You have entered an odd number')
