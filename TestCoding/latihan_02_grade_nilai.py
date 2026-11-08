# Soal 2: Menentukan grade dan kelulusan
# Konsep: if, elif, else, operator perbandingan

nilai = int(input("Masukkan nilai (0-100): "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("Grade: A")
    print("Status: Lulus")
elif nilai >= 75:
    print("Grade: B")
    print("Status: Lulus")
elif nilai >= 65:
    print("Grade: C")
    print("Status: Lulus")
elif nilai >= 50:
    print("Grade: D")
    print("Status: Tidak Lulus")
else:
    print("Grade: E")
    print("Status: Tidak Lulus")

# Penjelasan:
# Kondisi diperiksa dari nilai tertinggi ke terendah.
# elif dijalankan hanya jika kondisi sebelumnya tidak terpenuhi.
