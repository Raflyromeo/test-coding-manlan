nilai = int(input("Masukkan nilai mahasiswa: "))

if nilai < 0 or nilai > 100:
    print("Nilai yang dimasukkan tidak valid, Mohon masukkan nilai antara 0 sampai 100")
elif nilai >= 85:
    print("Status kelulusan mahasiswa: Mahasiswa dinyatakan lulus dengan predikat A")
elif nilai >= 75:
    print("Status kelulusan mahasiswa: Mahasiswa dinyatakan lulus dengan predikat B")
elif nilai >= 65:
    print("Status kelulusan mahasiswa: Mahasiswa dinyatakan lulus dengan predikat C")
elif nilai >= 50:
    print("Status kelulusan mahasiswa: Mahasiswa dinyatakan lulus dengan predikat D")
else:
    print("Status kelulusan mahasiswa: Mahasiswa dinyatakan tidak lulus dengan predikat E")