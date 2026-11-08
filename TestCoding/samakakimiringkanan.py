tinggi = int(input("Masukkan tinggi: "))
skala = 2

def baris(i):
    return "*" * max(1, (i - 1) * skala)

for i in range(1, tinggi + 1):
    print(baris(i))

for i in range(tinggi - 1, 0, -1):
    print(baris(i))