l = ["eat","tea","tan","ate","nat","bat", "cat", "ant"]

d = {}
for word in l:
    t = "".join(sorted(word))
    if d.get(t) != None:
        d[t].append(word)
    else:
        d[t] = [word]

print(list(d.values()))

