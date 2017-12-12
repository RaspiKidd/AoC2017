from collections import defaultdict

def problem(d):
    dd = defaultdict(set)

    for line in d:
        tokens = line.replace(",","").split()
        node, connections = int(tokens[0]), map(int,tokens[2:])
        for item in connections:
            dd[node].add(item)
            dd[item].add(node)

    # groupnodes starts with all nodes that need to be accounted for in a grouping
    groupNodes = set(dd.keys())

    # now start with a node and merge adjacents
    # any node that got accounted for in a flattening gets
    # discarded from the groupnode set
    def flatten(n):
        prevl = 0
        length = len(dd[n])
        groupNodes.discard(n)

        # Keep merging in sets until the length stops growing from
        # doing so
        while length != prevl:
            items = list(dd[n])
            for item in items:
                dd[n] |= dd[item]
                groupNodes.discard(item)
            prevl = length
            length = len(dd[n])

    flatten(0)
    print "part 1:", len(dd[0])

    # flatten all remaining nodes in the groupnodes set until every node has been processed
    # there will be one new group per pass
    count = 1
    while len(groupNodes):
        n = groupNodes.pop()
        flatten(n)
        count += 1

    print "part 2:", count

if __name__ == "__main__":
    problem(open("data.txt").readlines())
