# Soal 17: Menghitung angka positif, negatif, dan nol
# Konsep: for, if-elif-else, counter

jumlah = int(input("Berapa angka yang ingin dimasukkan? "))

if jumlah < 0:
    print("Jumlah tidak boleh negatif.")
else:
    positif = 0
    negatif = 0
    nol = 0

    for i in range(jumlah):
        angka = int(input(f"Masukkan angka ke-{i + 1}: "))

        if angka > 0:
            positif += 1
        elif angka < 0:
            negatif += 1
        else:
            nol += 1

    print("Jumlah positif:", positif)
    print("Jumlah negatif:", negatif)
    print("Jumlah nol:", nol)

# Penjelasan:
# Setiap input dikategorikan, lalu counter yang sesuai ditambah satu.
