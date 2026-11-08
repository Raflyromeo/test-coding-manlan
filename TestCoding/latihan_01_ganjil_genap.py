# Soal 1: Menentukan bilangan ganjil atau genap
# Konsep: input, int, modulus (%), if-else

angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print(f"Angka {angka} adalah Genap")
else:
    print(f"Angka {angka} adalah Ganjil")

# Penjelasan:
# Jika sisa pembagian angka dengan 2 adalah 0, angka termasuk genap.
# Selain itu, angka termasuk ganjil.
