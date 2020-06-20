#Python Dictionaries - associative array
x = 2
x = 4
print(x)
#4
#Associative arrays - Perl/PHP
#Properties or Map or Hashmap - Java
#Property Bag - C#/.Net

#making a dictionary
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
#{'money': 12, 'tissues': 75, 'candy': 3}
print(purse['candy'])
#3
purse['candy'] = purse['candy'] + 2
print(purse)
{'money': 12, 'tissues': 75, 'candy': 5}

#constants
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
{'jan': 100, 'chuck': 1, 'fred': 42}
ooo = {}
print(ooo)
{}

#counting with Dictionaries
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
#{'csev': 1, 'cwen': 1}
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
#{'csev': 1, 'cwen': 2}

#when we see a new name**no key in dictionary
counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        count[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
#{'csev': 2, 'zqian': 1, 'cwen': 2}

#or use
#get method
x = counts.get(name, 0)
#{'csev': 2, 'zqian': 1, 'cwen': 2}

#simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
#{'csev': 2, 'zqian': 1, 'cwen': 2}

#Counting Pattern
counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

#Definite loops and Dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
#jan 100
#chuck 1
#fred 42

#Retrieving lists of Keys and Values
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))
#['jan', 'chuck', 'fred']
print(jjj.keys())
#['jan', 'chuck', 'fred']
print(jjj.values())
#[100, 1, 42]
print(jjj.items())
#[('jan', 100), ('chuck', 1), ('fred', 42)]

#Two Iteration Variables
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa, bbb in jjj.items():
    print(aaa, bbb)
#jan 100
#chuck 1
#fred 42

name = input('Enter file:')
handle = open(name)

#Find the most words
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount: #maximumloop
        bigword = word
        bigcount = count

print(bigword, bigcount)





















































:




:
