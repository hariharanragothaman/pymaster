import itertools

string = "11122333444555677"
groups = []
for _, v in itertools.groupby(string):
    groups.append(len(list(v)))
print(groups)
