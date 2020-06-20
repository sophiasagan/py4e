text = "X-DSPAM-Confidence: 0.8475"
slice = text.find(':')
#print(slice)
piece = text[slice+2:]
#print(piece)
value = float(piece)
print(value)
