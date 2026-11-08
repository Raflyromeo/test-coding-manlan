tinggi = int(input("Masukkan tinggi: "))

for i in range(tinggi, 0, -1):
    for j in range(i):
        print("*", end="")

    print()