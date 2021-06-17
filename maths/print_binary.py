n = 5
length = 10

# here length is the length of the binary string - it takes care of zero padding
_f = "0" + str(length) + "b"
res = format(n, _f)
print(res)

# If I want the 0b infront of it
_f = '#' + "0" + str(length) + "b"