import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_83057.txt"
fh = open(fname)
y = list()
for line in fh:
    y.append(re.findall('[0-9]+',line))
sumtotal = 0
count = 0
for x in y:
    if len(x) > 0:
        for i in x:
            sumtotal += int(i)
            count += 1
print("There are " + str(counter) + " numbers, which sum to " + str(sumtotal))
