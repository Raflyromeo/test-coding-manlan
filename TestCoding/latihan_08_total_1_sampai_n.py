# Soal 8: Menghitung jumlah 1 sampai N
# Konsep: for dan accumulator

n = int(input("Masukkan angka: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Total:", total)

# Penjelasan:
# total adalah accumulator yang menyimpan hasil penjumlahan.
