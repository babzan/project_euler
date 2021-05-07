#####################################
# Just find any number from 1 to 1000
# which multiples to 3 and 5
# and then we calculate their sum
#####################################

i = 1
new_list = []
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        new_list.append(i)
    i += 1

print('Sum of multiples of 3 and 5 to 1000 is:', sum(new_list))