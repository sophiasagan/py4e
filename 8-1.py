loop through the text to get the lines
   loop through the lines to get the words
      if a word is not in the empty list
         append it

sort
print

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
line_list = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    for word in wds:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
