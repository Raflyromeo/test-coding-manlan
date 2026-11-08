tinggi = int(input("Masukkan tinggi: "))

for i in range(1, tinggi + 1):
    for j in range(tinggi - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

for i in range(tinggi - 1, 0, -1):
    for j in range(tinggi - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()