from collections import defaultdict

s = "bbbaaaba"
t = "aaabbbba"

map_s = defaultdict(list)
map_t = defaultdict(list)

for index, value in enumerate(s):
    if value not in map_s:
        map_s[value] = [index]
    else:
        map_s[value].append(index)

for index, value in enumerate(t):
    if value not in map_t:
        map_t[value] = [index]
    else:
        map_t[value].append(index)

if len(map_s.keys()) == len(map_t.keys()):
    for i in map_s.values():
        if i not in map_t.values():
            print("False")
    print("True")
else:
    print("False")
