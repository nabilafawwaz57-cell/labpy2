# Program mengurutkan data dari yang terkecil ke terbesar

print("Program Mengurutkan Data")

# Input jumlah data minimal 3
n = int(input("Masukkan jumlah bilangan (minimal 3): "))

# Validasi agar minimal 3 data
if n < 3:
    print("Minimal harus 3 bilangan")
else:
    data = []
    for i in range(n):
        bil = int(input(f"Bilangan ke-{i+1}: "))
        data.append(bil)

    # Mengurutkan data
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                # Tukar posisi bila data tidak urut
                data[i], data[j] = data[j], data[i]

    # Tampilkan hasil
    print("Urutan bilangan (dari terkecil):", *data)
