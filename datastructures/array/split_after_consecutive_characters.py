# -*- coding: utf-8 -*-
# @Author: Hariharan Ragothaman
# @Date:   2022-04-22 16:59:23
# @Last Modified by:   Hariharan Ragothaman
# @Last Modified time: 2022-04-22 17:02:30


def split_into_same_char_segments(s):
	n, ans, ch = len(s), [], ''
	
	for i in range(n-1):
		if s[i] == s[i+1]:
			ch += s[i]
		elif s[i] != s[i+1]:
			ch += s[i]
			ans.append(ch)
			ch = ''
	if ch:
		ch += s[-1]
		ans.append(ch)
	else:
		ans.append(s[-1])
	print(ans)

split_into_same_char_segments("aaaabbbab")