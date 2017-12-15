startA, startB = 591, 393
genA, genB = 16807, 48271
mod = 2147483647
a = startA
b = startB
same = 0

for _ in xrange(40 * 10 **6):
  if (a & 0xffff) == (b & 0xffff):
    same += 1
  a = (a * genA) % mod
  b = (b * genB) % mod
print same

a = startA
b = startB
generated_as = []
generated_bs = []
while True:
  a = (a * genA) % mod
  if (a & 3) == 0:
    generated_as.append(a)
  b = (b * genB) % mod
  if (b & 7) == 0:
    generated_bs.append(b)
  if min(len(generated_as), len(generated_bs)) > (5 * 10**6):
    break

print len(filter(lambda (a,b): (a & 0xffff) == (b & 0xffff), zip(generated_as, generated_bs)[:5*10**6]))
