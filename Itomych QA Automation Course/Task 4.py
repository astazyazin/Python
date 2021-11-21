import copy

with open("INPUT.TXT", "r") as somefile:
    numb = int(somefile.read())
rez = 'Yes'
dividers = [1000, 100, 10, 1]
ost = []
for i in dividers:
    ost.append((numb // i))
    numb %= i

ost_reverse =  copy.deepcopy(ost)
ost.reverse()
i = 0
while i < len(ost):
    if ost[i] != ost_reverse[i]:
        rez = 'No'
    i += 1
with open("OUTPUT.TXT", "w") as somefile1:
    somefile1.write(rez)
