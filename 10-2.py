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
            tracker[wds[5]] = tracker.get(wds[5],0) + 1

times = list()
hrs = dict()
for k,v in tracker.items():
    times.append(k.split(':'))
for time in times:
    hrs[time[0]] = hrs.get(time[0],0) + 1
thesort = sorted([(k,v) for k,v in hrs.items()])
for j in thesort:
    print(j[0],j[1])

    10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
