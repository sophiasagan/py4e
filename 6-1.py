#lenfunction
fruit = 'banana'
x = len(fruit)
print(x)
#looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    x = fruit[index]
    print(index, x)
    index = index + 1
#looping through strings preferred/simple
fruit = 'banana'
for letter in fruit:
    print(letter)
#looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
#slicing strings
s = 'Monty Python'
print(s[0:4])
#Mont #"up to but not including"
print(s[6:7])
#string concatenation
a = 'Hello'
b = a + 'There'
print(b)
#HelloThere
c = a + ' ' + 'There'
print(c)
Hello There
#Using in as a logical operator
fruit = 'banana'
'n' in fruit
#True
'm' in fruit
#False
'nan' in fruit
#True
if 'a' in fruit:
    print('Found it!')
#Found it!
#String Comparison
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word >'banana':
    print('Your word,') + word + ', comes after banana.')
else:
    print('All right, bananas.')
#String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
#hello bob
print(greet)
#Hello Bob
print('Hi There'.lower())
#hi there
#searching a string
fruit = 'banana'
pos = fruit.find('na')
print(pos)
#2
aa = fruit.find('z')
print(aa)
#-1
#Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
#Hello Jane
nstr = greet.replace('o', 'X')
print(nstr)
#HellX BXb
#Stripping Whitespace
greet = '   Hello bob   '
greet.lstrip()
#'Hello Bob'
greet.rstrip()
#'  Hello Bob'
greet.strip()
#'Hello Bob'
#Prefixes
line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')
#False
#Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jane5 09:14:16 2006'
atpos = data.find('@')
print(atpos)
#21
sppos = data.find(' ',atpos)
print(sppos)
#31
host = data[atpos+1 : sppos]
print(host)
#uct.ac.za
