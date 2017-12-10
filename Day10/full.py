def reverse(text, repeat):
     knot = list(range(256))
     position = 0
     skip = 0
     for isntevenused in range(repeat):
          for i in text:
             temp = []
             for j in range(i):
                 temp.append(knot[(position+j) % 256])
             for j in range(i):
                 knot[(position+i-1-j) % 256] = temp[j]
             position += skip + i
             skip += 1
     return knot


def dense(knot):
     dense = [0]*16
     for i in range(16):
         dense[i] = knot[16*i]
         for m in range(1, 16):
             dense[i] ^= knot[16*i+m]
     return dense


def kH(dense):
     knotHash = ''
     for i in dense:
         if len(hex(i)[2:]) == 2:
             knotHash += hex(i)[2:]
         else:
             knotHash += '0' + hex(i)[2:]
     return knotHash


inp = '102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'
txt = [102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216]
txt2 = []

for i in range(len(inp)):
     txt2.append(ord(inp[i]))
txt2 += [17, 31, 73, 47, 23]

knot = reverse(txt, 1)
sparce = reverse(txt2, 64)

dense = dense(sparce)
knotHash = kH(dense)

print('Part 1: ' + str(knot[0]*knot[1]))
print ('Part 2: ' + knotHash)
