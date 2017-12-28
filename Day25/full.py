from collections import defaultdict

tape = defaultdict(int)

states = {'A':[[1,1,'B'],[0,-1,'B']],
          'B':[[0,1,'C'],[1,-1,'B']],
          'C':[[1,1,'D'],[0,-1,'A']],
          'D':[[1,-1,'E'],[1,-1,'F']],
          'E':[[1,-1,'A'],[0,-1,'D']],
          'F':[[1,1,'A'],[1,-1,'E']]}

cursor = 0
state = 'A'
#positions = {}
#checksumafter = 12629077
'''
for s in range(checksumafter):
    ns =  positions.get(currpos, 0)
    positions[currpos]= states[currstate][ns][0]
    currpos += states[currstate][ns][1]
    currstate = states[currstate][ns][2]

print(len([x for x in positions if positions[x]]))
'''

for i in xrange(12629077):
    current_value = tape[cursor]
    write, move, next_state = states[state][current_value]
    if write:
        tape[cursor] = write
    else:
        del tape[cursor]
    cursor += move
    state = next_state

print len(tape)
