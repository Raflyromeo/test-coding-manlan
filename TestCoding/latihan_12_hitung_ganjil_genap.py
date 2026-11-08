# Soal 12: Menghitung banyak bilangan ganjil dan genap dari 1 sampai N
# Konsep: for, if-else, counter

n = int(input("Masukkan angka: "))

ganjil = 0
genap = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print("Jumlah bilangan ganjil:", ganjil)
print("Jumlah bilangan genap:", genap)

# Penjelasan:
# Counter ganjil dan genap bertambah setiap kali kondisi ditemukan.
