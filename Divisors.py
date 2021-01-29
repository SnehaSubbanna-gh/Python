num = input("Please enter a number : ")
number = int(num)
i = 1
divisors = []
while i <= number:
    if number % i == 0:
        divisors.append(i)
    i = i + 1

print(f"The divisors of {num} are {divisors}")