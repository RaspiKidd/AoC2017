import string
from collections import deque


def parse_input(c, d):
    if c in string.ascii_lowercase:
        return d[c]
    return int(c)


def part1(lines):
    d = {k:0 for k in string.ascii_lowercase}
    len_lines = len(lines)
    index = 0
    last_snd = None
    while True:
        command = lines[index].split(" ")
        if command[0] == 'set':
            d[command[1]] = parse_input(command[2], d)
        elif command[0] == 'add':
            d[command[1]] += parse_input(command[2], d)
        elif command[0] == 'mul':
            d[command[1]] *= parse_input(command[2], d)
        elif command[0] == 'mod':
            d[command[1]] = d[command[1]] % parse_input(command[2], d)
        elif command[0] == 'snd':
            last_snd = d[command[1]]
        elif command[0] == 'rcv':
            if parse_input(command[1], d) != 0:
                return last_snd
        elif command[0] == 'jgz':
            if parse_input(command[1], d) > 0:
                index += parse_input(command[2], d)
                continue
        index += 1
        if index >= len_lines - 1:
            break


def part2(lines):
    gen0 = Program(lines, {'p': 0})
    gen1 = Program(lines, {'p': 1})
    send_count = 0
    d1 = deque()

    while True:
        try:
            cmd1 = next(gen1)
        except StopIteration:
            return send_count
        if cmd1[0] == 'snd':
            send_count += 1
            d1.appendleft(cmd1)
        else:
            while True:
                try:
                    cmd0 = next(gen0)
                except StopIteration:
                    return send_count
                if cmd0[0] == 'snd':
                    gen1.receive(cmd0)
                    break
                else:
                    try:
                        gen0.receive(d1.pop())
                    except IndexError:
                        return send_count


class Program:
    def __init__(self, lines, initial_dict=None):
        self.d = {**{k:0 for k in string.ascii_lowercase}, **(initial_dict or {})}
        self.lines = lines
        self.len_lines = len(lines)

        self._index = 0
        self._receive_lock = False
        self._receiving_register = None

    def receive(self, command):
        self.d[self._receiving_register] = command[1]
        self._receive_lock = False
        self._receiving_register = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self._receive_lock:
            while True:
                if self._index > self.len_lines - 1:
                    raise StopIteration
                command = self.lines[self._index].split(" ")

                if command[0] == 'set':
                    self.d[command[1]] = parse_input(command[2], self.d)
                elif command[0] == 'add':
                    self.d[command[1]] += parse_input(command[2], self.d)
                elif command[0] == 'mul':
                    self.d[command[1]] *= parse_input(command[2], self.d)
                elif command[0] == 'mod':
                    self.d[command[1]] = self.d[command[1]] % parse_input(command[2], self.d)
                elif command[0] == 'jgz':
                    if parse_input(command[1], self.d) > 0:
                        self._index += parse_input(command[2], self.d)
                        continue
                elif command[0] == 'snd':
                    self._index += 1
                    return ('snd', parse_input(command[1], self.d))
                else:
                    self._receive_lock = True
                    self._receiving_register = command[1]
                    self._index += 1
                    return command
                self._index += 1



with open('data.txt') as f:
    s = f.read().strip()
    s = s.splitlines()

print(part1(s))
print(part2(s))
