# Soal 14: Kasir sederhana dengan diskon
# Konsep: input, operasi aritmatika, if-else

harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

if harga < 0 or jumlah <= 0:
    print("Harga atau jumlah barang tidak valid.")
else:
    subtotal = harga * jumlah

    if subtotal >= 100000:
        diskon = subtotal * 0.10
    else:
        diskon = 0

    total = subtotal - diskon

    print(f"Subtotal: Rp{subtotal:,.0f}")
    print(f"Diskon: Rp{diskon:,.0f}")
    print(f"Total pembayaran: Rp{total:,.0f}")

# Penjelasan:
# Diskon 10% diberikan jika subtotal minimal Rp100.000.
