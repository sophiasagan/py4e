fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
words = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    try:
        if words[0] == "From":
            count += 1
            lst.append(words[1])
            print(words[1])
    except:
        continue
print("There were", count, "lines in the file with From as the first word")
#or
fname = input("Enter file name: ")

for line in fname:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
