# -*- coding: utf-8 -*-
# File              : reverse_string.py
# Author            : cppygod
# Date              : 07.11.2022
# Last Modified Date: 07.11.2022
# Last Modified By  : cppygod

s = 'helloworld'


def recur(word, n, i, j):
    # Identify the base condition
    if i > j:
        return word
    if i < j:
        # This is the core idea
        word[i], word[j] = word[j], word[i]
        # The variables that control the recursion are also passed
        # This returns the modified controlled variables to the next recursion call
        return recur(word, n, i+1, j-1)

    print(word)

n = len(s)
i, j = 0, n-1
s = [c for c in s]
ans = recur(s, n, i, j)
print(''.join(ans))
