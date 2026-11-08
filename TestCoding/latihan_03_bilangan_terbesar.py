# Soal 3: Menentukan bilangan terbesar dari tiga angka
# Konsep: if-elif-else, operator and

a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))
c = float(input("Angka ketiga: "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print("Bilangan terbesar adalah:", terbesar)

# Penjelasan:
# and berarti kedua kondisi harus benar.
# Operator >= juga menangani kondisi ketika ada angka yang sama.
