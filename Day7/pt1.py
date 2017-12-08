import re

with open ('data.txt') as f:
    data = f.read().splitlines()

all_nodes = []
all_supported = []
for line in data:
    all_nodes.append(re.match(r'[\w]+', line).group(0))
    if re.search(r'->', line):
            nodes = re.search(r'-> (?P<nodes>[\w, ]+)', line).group('nodes').replace(' ', '').split(',')
            for node in nodes:
                all_supported.append(node)
print(set(all_nodes) - set(all_supported))
