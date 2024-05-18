#Exercise 1.
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

nums = range(1, 100)
print("Ex 1.\nPrime numbers form 2 to 100: ", list(i for i in nums if isPrime(i)), '\n')


#Exercise 2

import decimal as dec
import statistics as stat

print("Ex 2. Calculating the income on our bank deposit over 10 years with 5% interest rate annually")
deposit = dec.Decimal('1000.00')
percent = dec.Decimal('0.05')
print(f'Year:{"State of the deposit:":>25}')
for year in range(1, 11):
    state = deposit * (1 + percent) ** year
    print(f'{year:>2}{state:>17.2f}')
print('\n')
    
    
#Exercise 3

print("Ex 3. Simple diagram: ")
print(f'{"Index:"}{"Value:":>8}{"Graph:":>8}')

listA = [12, 13, 24, 5, 10, 6, 1, 6, 4]

list_mean = stat.mean(listA)
list_median = stat.median(listA)
list_mode = stat.mode(listA)

for key, value in enumerate(listA, start=1):
    print(f'{key:>4}{value:>9}{" ":>3}{"*" * value}')

print("\nMean: ", list_mean, "\nMedian: ", list_mean, "\nMode: ", list_mode, '\n')


#Exercise 4

print("Ex 4. Testing functions 'map' and 'filter':\n")

listB = [-12, 14, 7, 15, 51, 241, 123, 61, 14, 51]

print("List:", listB)
print("Even:", list(filter(lambda x: x % 2 != 0, listB)))
print("To the power of 2:", [x ** 2 for x in listB])
print("To the power of 3 (reversed):", [x ** 3 for x in reversed(listB)])
print("To the power of 2 (map + lambda):", list(map(lambda x: x ** 2, listB)))
print("To the power of 2 (filter + lambda):", list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, listB))))


print("Sorted ASC:", sorted(listB))
print("Sorted DESC:", sorted(listB, key=None, reverse=True))
print("Sum:", sum(listB))

#sorted(kolory, key = lambda x: x.lower())
















