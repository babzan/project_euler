#####################################
# Find all prime factors of number
# 600851475143 (or else if you want)
# and then print the max prime factor
#####################################

def prime_factors(num):
    i = 2
    while i < num:
        if num % i == 0:
            num = num // i
            list_of_prime_factors.append(i)
            i = 1
        i += 1
    list_of_prime_factors.append(num)
    return list_of_prime_factors


print('Please, enter a number for calculating their max prime factor: ')
num = int(input())
list_of_prime_factors = []
print('Max prime factor of {} is:'.format(num), max(prime_factors(num)))
