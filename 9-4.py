fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

count = 0
tracker = dict()
wds = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) > 0 and wds[0] == "From":
            tracker[wds[1]] = tracker.get(wds[1],0) + 1
#print(tracker)

bigkey = None
bignumber = None

for word,count in tracker.items():
    if bignumber is None or count > bignumber:
        bigkey = word
        bignumber = count

print(bigkey, bignumber)
