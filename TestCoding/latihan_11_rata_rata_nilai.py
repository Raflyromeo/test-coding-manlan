# Soal 11: Menghitung rata-rata nilai
# Konsep: for, accumulator, if-else

jumlah = int(input("Jumlah mata kuliah: "))

if jumlah <= 0:
    print("Jumlah mata kuliah harus lebih dari 0.")
else:
    total = 0

    for i in range(1, jumlah + 1):
        nilai = float(input(f"Nilai mata kuliah {i}: "))
        total += nilai

    rata_rata = total / jumlah

    print("Total nilai:", total)
    print("Rata-rata:", rata_rata)

    if rata_rata >= 75:
        print("Status: Lulus")
    else:
        print("Status: Tidak Lulus")

# Penjelasan:
# Nilai dijumlahkan satu per satu, lalu dibagi jumlah mata kuliah.
