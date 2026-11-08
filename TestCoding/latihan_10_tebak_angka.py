# Soal 10: Permainan tebak angka
# Konsep: while, if-elif-else, break

angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print("Tebakan benar!")
        break

# Penjelasan:
# while True mengulang terus.
# break menghentikan perulangan ketika tebakan benar.
