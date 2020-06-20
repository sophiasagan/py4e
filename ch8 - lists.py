List Constants

print([1, 24, 76])
#[1, 24, 76]
print(['red', 'yellow', 'blue'])
#['red', 'yellow', 'blue']
print(['red', 24, 98.6])
#['red', 24, 98.6]
print([1, [5, 6], 7])
#[1, [5, 6], 7]
print([])
#[]

#lists and definite loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

#same code as above
z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')

#Lists are mutable
fruit = 'Banana'
fruit[0] = 'b'
#traceback
x = fruit.lower()
print(x)
#banana
lotto = [2, 14, 26, 41, 63]
print(lotto)
#[2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto)
#[2, 14, 28, 41, 63]

#How long is a list?
greet = 'Hello Bob'
print(len(greet))
#9
x = [1, 2, 'joe', 99]
print(len(x))
#4

#Range Function - returns a list (up to but not including)
print(range(4))
[0, 1, 2, 3]
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
#3
print(range(len(friends)))
#[0, 1, 2]
#does the same thing
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
#concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
#[1, 2 ,,3, 4, 5, 6]
print(a)
#[1, 2, 3]

#slicing
t = [9, 41, 12, 3, 74, 15]
t[1:3]
#[41, 12]
t[:4]
#[9, 41, 12, 3]
t[3:]
#[3, 74, 15]
t[:]
#[9, 41, 12, 3, 74, 15]

#building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
#['book', 99]
stuff.append('cookie')
print(stuff)
#['book', 99, 'cookie']

#Is something in a list
some = [1, 9, 21, 10, 16]
9 in some
#True
15 in some
#False
20 not in some
#True

#Lists are in order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
#['Glenn', 'Joseph', 'Sally']
print(friends[1])
#Joseph

#Built-in Functions
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
#6
print(max(nums))
#74
print(min(nums))
#3
print(sum(nums))
#154
print(sum(nums)/len(nums))
#25.6

#Calculating Average
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)

#Strings and lists
abc = 'With three words'
stuff = abc.split()
print(stuff)
#['With', 'three', 'words']
print(len(stuff))
#3
print(stuff[0])
#with
print(stuff)
['With', 'three', 'words']
for w in stuff :
    print(w)
#With
#Three
#Words

#Delimiter
line = 'A lot               of spaces'
etc = line.split()
print(etc)
#['A', 'lot', 'of', 'spaces']
line = 'first;second;third'
thing = line.split(:)
print(thing)
#['first';'second';'third']
print(len(thing))
#3

#parsing the mail data
#From stephen.marquard@uct.a.za Sat Jan 5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
#Sat

line = 'From stephen.marquard@uct.a.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)
#['From', 'stephen.marquard@uct.a.za', 'Sat', 'Jan', '5', '09:14:16', '2008']

words = line.split[]
email = words[1]
pieces = email.split('@')
print(pieces[1])
#uct.ac.za
