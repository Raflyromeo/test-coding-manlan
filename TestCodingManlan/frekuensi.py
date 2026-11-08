# 2. buat program menghitung frekeunsi kemunculan setiap angka dalam setiap list datanya 2,3,2,2,5,3,2,7,5 outputnya: 2 muncul 3x, 3 muncul 2x, 5 muncul 2x. 7 muncul 1x

data = [2,3,2,2,5,3,7,5]

frekuensi = {}
for angka in data:
    frekuensi[angka] = frekuensi.get(angka, 0) + 1

for angka, count in frekuensi.items():
    print(f"{angka} muncul {count}x")