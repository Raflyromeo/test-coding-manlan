# Soal 15: Menu utama dengan while dan match-case
# Membutuhkan Python 3.10 atau lebih baru.

while True:
    print("\n===== MENU UTAMA =====")
    print("1. Cek Ganjil Genap")
    print("2. Luas Persegi")
    print("3. Luas Segitiga")
    print("4. Keluar")

    pilihan = int(input("Pilih menu: "))

    match pilihan:
        case 1:
            angka = int(input("Masukkan angka: "))
            if angka % 2 == 0:
                print("Bilangan Genap")
            else:
                print("Bilangan Ganjil")

        case 2:
            sisi = float(input("Masukkan sisi: "))
            print("Luas persegi:", sisi * sisi)

        case 3:
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Luas segitiga:", 0.5 * alas * tinggi)

        case 4:
            print("Terima kasih!")
            break

        case _:
            print("Pilihan tidak tersedia!")

# Penjelasan:
# while menjaga menu tetap tampil.
# match-case memilih tindakan berdasarkan menu.
# break mengakhiri program saat pengguna memilih 4.
