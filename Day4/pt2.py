with open ('data.txt') as open_file:
    a = open_file.read().splitlines()

total = 0

for line in a:
    if line in a:
        words_array = list(map(lambda x: ('').join(sorted(list (x))), line.split()))
        if len (words_array) == len(set(words_array)):
            total += 1

print (total)
