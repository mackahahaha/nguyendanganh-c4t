text = str(input("what do you want to type?:")).lower()
d = dict.fromkeys(text, 0)
list = list(d)
n = sorted(list, key = str.lower)
dict = dict.fromkeys(n, 0)
for c in text: dict[c] += 1
sorted(text, key=str.lower)
for k, v in dict.items():
    if k != ' ' and k != ".":
        print(k,end=' ')
        print(v)
input("Enter to exit")