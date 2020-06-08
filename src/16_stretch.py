# Python program to check if given number id prime or not
import sys 

len = len(sys.argv)

if len < 2:
    print('Please follow this format: 16_stretch.py number')
    sys.exit()

num = sys.argv[1]
num = int(num)
if num > 1:
    
    for i in range(2, num):
        # if num is divisible by any number between 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(f'False. {num} is not a prime number')
            break
    else:
        print(f'True. {num} is a prime number')
else: 
    print(f'False. {num} is not a prime number')

