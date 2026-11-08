# Soal 5: Menentukan tahun kabisat
# Konsep: if-elif-else dan modulus

tahun = int(input("Masukkan tahun: "))

if tahun % 400 == 0:
    print("Tahun kabisat")
elif tahun % 100 == 0:
    print("Bukan tahun kabisat")
elif tahun % 4 == 0:
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")

# Penjelasan:
# Tahun yang habis dibagi 400 adalah kabisat.
# Jika habis dibagi 100 tetapi tidak 400, bukan kabisat.
# Jika habis dibagi 4 tetapi tidak 100, kabisat.
