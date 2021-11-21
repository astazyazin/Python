rez = 0
i = 1
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        rez += i
    i += 1
print(rez)
