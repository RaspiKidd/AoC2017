with open ('data.txt') as f :
    a = f.readlines ()

total = 0

for line in a:
    b = line.split ()
    c = set (b)
    if len (b) == len (c):
        total += 1

print (total)
