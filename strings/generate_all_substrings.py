# To generate all possible sub-strings - brute-force
strs = "Success"
for i in range(len(strs)):
    for j in range(i + 1, len(strs) + 1):
        print(strs[i:j])