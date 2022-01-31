a="      asasa dfdfdfd hghghghghghgh         "
a=a.strip()
b=a.split(" ")
print(b)
c=[len(i) for i in b]
print(b[c.index(max(c))])