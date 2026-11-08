# Soal 18: Sistem perpustakaan sederhana
# Membutuhkan Python 3.10 atau lebih baru.
# Konsep: while, match-case, if-else, update variabel

stok = 10

while True:
    print("\n=== PERPUSTAKAAN ===")
    print("1. Lihat jumlah buku")
    print("2. Pinjam buku")
    print("3. Kembalikan buku")
    print("4. Keluar")

    pilihan = int(input("Pilih menu: "))

    match pilihan:
        case 1:
            print("Stok buku:", stok)

        case 2:
            jumlah = int(input("Jumlah buku yang dipinjam: "))

            if 0 < jumlah <= stok:
                stok -= jumlah
                print("Buku berhasil dipinjam.")
                print("Sisa stok:", stok)
            else:
                print("Jumlah tidak valid atau stok tidak mencukupi.")

        case 3:
            jumlah = int(input("Jumlah buku yang dikembalikan: "))

            if jumlah > 0:
                stok += jumlah
                print("Buku berhasil dikembalikan.")
                print("Stok sekarang:", stok)
            else:
                print("Jumlah pengembalian harus lebih dari 0.")

        case 4:
            print("Program selesai.")
            break

        case _:
            print("Pilihan tidak tersedia.")

# Penjelasan:
# Stok berkurang saat peminjaman dan bertambah saat pengembalian.
# Validasi mencegah peminjaman melebihi stok dan jumlah negatif.
