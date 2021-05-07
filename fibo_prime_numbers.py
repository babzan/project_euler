###################################
# Find Fibonacci numbers to some
# entered number (sum) which even
# and then calculate their sum
###################################

a = b = 1
print('Please enter the end number:')
end_number = int(input())
res = 0
new_list = []
while a and b < end_number:
    res = a + b
    a = b
    b = res
    if res % 2 == 0:
        new_list.append(res)
print('Sum of even Fibonacci numbers is:', sum(new_list))
