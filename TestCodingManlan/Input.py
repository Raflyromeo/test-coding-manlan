# 1. Buat program menerima 5 angka dari user kemudia tampilkan 3 point yaitu nilai terbesar terkecil rata rata dari 5 angka tsb

user_input = input("Masukkan 5 angka:" )

if user_input:
    angka_list = user_input.split(",")
    angka_list = [int(angka) for angka in angka_list]

    if len(angka_list) == 5:
        nilai_terbesar = max(angka_list)
        nilai_terkecil = min(angka_list)
        rata_rata = sum(angka_list) / len(angka_list)

        print("Nilai terbesar:", nilai_terbesar)
        print("Nilai terkecil:", nilai_terkecil)
        print("Rata-rata:", rata_rata)
    else:
        print("Harap masukkan tepat 5 angka.")