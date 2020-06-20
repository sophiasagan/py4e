for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
*****
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print ('Done')
******basicloop.py
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')
****largest.py
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
*****countloop.py
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
*****summingloop.py
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)
**********averageloop.py
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count):
********filterloop.py
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print 'Large number', value
print('After')
*****booleanvariableloop.py
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)
print ('After', found)
******smallest.py
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smalles = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
