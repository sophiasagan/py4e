#Ch11Regular_Expressions
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end


import re - import regular Expression library
re.search() - to see if a string matches a regular Expression
re.findall() - to extract portions of a string that match your regular expression.
    similar to a combination of find() and slicing: var[5:10]

#example using re.search() like find()
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)
#using re.search() like startswith()
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)

#Wild-Card Expressions
dot character matches any character
if you add asterisk character, the character is "any number of times"
^X.*:
#X-Sieve: CMU Sieve 2.3
#X-DSPAM-Result: Innocent
#X-DSPAM-Confidece: 0.8475
#X-Content-Type-Message-Body: text/plain
^X-\S+:
#match the start of the line X-; Match any non-whitespace character\S;
#one or more times+

#matching and extracting data
re.search() returns a t/f depending on whether the string matches the regular Expression
re.findall()
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
#['2', '19', '42']
y = re.findall('[AEIOU]+', x)
print(y)
#[]

#Greedy Matching
The repeat character(*and+) push outward in both directions (greedy) to match
the largest possible string

#fine-tuning string extraction
y = re.findall('\S+@\S+', x)
print(y)
['stephen.marquard@uct.ac.za']
y = re.findall('^From (\S+@\S+)', x)
print(y)
['stephen.marquard@uct.ac.za']

#double split
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)
['uct.ac.za']

#Spam Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
#X-DSPAM-Confidence: 0.8475

#Escape character
if you want a special re to behave normally prefix with "\"
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+, x')
print(y)
#['$10.00']
