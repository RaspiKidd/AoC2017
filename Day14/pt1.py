inptpt1 = "jzgqcdpd"

def knotHash(data):
    data = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    l = range(256)
    i = 0
    skipSize = 0
    for _ in xrange(64):
        for d in data:
            for j in xrange(d / 2):
                l[(i + j) % len(l)], l[(i + (d - j - 1)) % len(l)] = l[(i + (d - j - 1)) % len(l)], l[(i + j) % len(l)]
            i += d + skipSize
            i = i % len(l)
            skipSize += 1

    denseHash = []
    for i in xrange(16):
        x = 0
        for j in xrange(16):
            x = x ^ l[i*16 + j]
        denseHash.append(x)
    s = ""
    for c in denseHash:
        s += "{0:02x}".format(c)
    return s

grid = []
for i in xrange(128):
     kh = knotHash("%s-%d" % (inpt, i))
     gridline = []
     for c in kh:
         gridline.extend([int(c) for c in "{0:04b}".format(int(c, 16))])
     grid.append(gridline)

# part 1
print sum(sum(gridline) for gridline in grid)
