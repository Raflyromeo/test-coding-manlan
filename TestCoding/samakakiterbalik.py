tinggi = int(input("Masukkan tinggi: "))

for i in range(tinggi, 0, -1):
    for j in range(tinggi - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()