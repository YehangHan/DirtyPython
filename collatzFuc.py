def collatz(number):
    res = 0
    if number % 2 == 0:
        res = (number//2)
        print(res)
    elif number % 2 == 1:
        res = 3 * number + 1
        print(res)
    return res   

print('Enter number:')
try:
    num = int(input())
    while num != 1:
        num = collatz(num)
except ValueError:
    print('Please input an integer.')


