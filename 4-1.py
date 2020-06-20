def computepay(fh,fr):
    return 42.37

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40:
    reghrs = fh * fr
    ovt = (fh - 40) * (fr * 0.5)
    p = reghrs + ovt
else:
    p = fh * fr

print(p)
