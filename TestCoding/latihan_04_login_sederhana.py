# Soal 4: Login sederhana
# Konsep: if-else, operator ==, operator and

username_benar = "admin"
password_benar = "manlan123"

username = input("Username: ")
password = input("Password: ")

if username == username_benar and password == password_benar:
    print("Login Berhasil!")
else:
    print("Login Gagal!")

# Penjelasan:
# Operator and mengharuskan username DAN password benar.
