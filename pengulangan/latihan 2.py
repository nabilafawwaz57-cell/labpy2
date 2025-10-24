import random

print("Program menampilkan n bilangan acak < 0.5")

# Input jumlah bilangan
n = int(input("Masukkan jumlah n: "))

count = 0  # penghitung jumlah bilangan yang sudah ditampilkan

# Loop menggunakan while dan for
while count < n:
    bil = random.random()  # menghasilkan angka acak antara 0.0 - 1.0
    if bil < 0.5:
        print(bil)
        count += 1
