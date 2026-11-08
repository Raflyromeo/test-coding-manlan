# Soal 6: Kalkulator sederhana menggunakan match-case
# Membutuhkan Python 3.10 atau lebih baru.

print("=== KALKULATOR ===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = int(input("Pilih operasi: "))
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))

match pilihan:
    case 1:
        print("Hasil:", a + b)
    case 2:
        print("Hasil:", a - b)
    case 3:
        print("Hasil:", a * b)
    case 4:
        if b != 0:
            print("Hasil:", a / b)
        else:
            print("Tidak bisa membagi dengan nol!")
    case _:
        print("Pilihan tidak tersedia")

# Penjelasan:
# match membandingkan pilihan dengan setiap case.
# case _ berfungsi sebagai pilihan default.
