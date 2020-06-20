#Ch10Tuples
#tuples are like Lists
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
#Joseph
y = (1, 9, 2)
print(y)
#(1, 9, 2)
print(max(y))
#9
#same in for loops

#tuples are not mutable - lists are
#can't sort/append/reverse/pop/remove
#can count and index

#tuples and assignments
(x,y) = (4, 'fred')
print(y)
#fred
(a, b) = (99, 98)
print(a)
99

#tuples are comparable
(0, 1, 2) < (5, 1, 2)
#True
(0, 1, 2000000) < ('Jones', 'Sam')
#True
('Jones', 'Sally') > ('Adams', 'Sam')
#True

#sorting lists of tuples
d = {'a': 10, 'b': 1, 'c': 22}
d.items()
#dict_items()[('a', 10), ('c', 22), ('b', 1)])

#Using sorted() - key order
d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
t
[('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(d.items()):
    print(k, v)
#a 10
#b 1
#c 22

#sort by values instead of key
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append( (v,k) )

print(tmp)
#[(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp, reverse=True)#sorting high to low by value
print(tmp)
#[(22, 'c'), (10, 'a'), (1, 'b')]

#10 most common Words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key,val)

#bottom half of code in one line
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v,k) for k,v in c.items()]))
#[(1, 'b'), (10, 'a'), (22, 'c')]


























,
