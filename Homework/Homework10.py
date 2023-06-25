import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
print(*lst)

print(f"\trobot\thuman")
for i in range(len(lst)):
    if lst[i] == "robot":
        print(f"{i}\t1\t0")
    else:
        print(f"{i}\t0\t1")
