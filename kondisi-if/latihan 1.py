# Program menentukan bilangan terbesar dari 4 bilangan menggunakan if

# Input 4 bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

# Menentukan bilangan terbesar
terbesar = a  # anggap a yang terbesar dulu

if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d

# Output hasil
print("Bilangan terbesar adalah:", terbesar)
