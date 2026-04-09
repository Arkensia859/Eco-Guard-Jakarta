print("GEROBAK FRIED CHICKEN".center(80))
print("".center(80, "-"))
print("Kode     Jenis Potongan Ayam".ljust(50) + "Harga".rjust(10))
print("D        Dada".ljust(50) + "Rp. 2500".rjust(10))
print("P        Paha ".ljust(50) + "Rp. 2000".rjust(10))
print("S        Sayap".ljust(50) + "Rp. 1500".rjust(10))
print()
print("".center(80, "-"))
print()

# Simpan semua entri ke dalam list sehingga setiap baris di output mewakili satu input.
orders_jenis = []
orders_harga = []
orders_jumlah = []
orders_total = []

try:
    ulang = int(input("Masukkan Banyak Jenis : "))
except ValueError:
    print("Input tidak valid. Menggunakan 0.")
    ulang = 0

for i in range(ulang):
    print("Jenis ke-" + str(i+1))
    kode = input("Masukkan Kode Potongan Ayam [D/P/S]: ").strip().lower()
    try:
        jumlah = int(input("Masukkan Jumlah Potong : "))
    except ValueError:
        print("Jumlah tidak valid, menggunakan 0")
        jumlah = 0

    if kode == "d":
        jenis = "Dada"
        harga = 2500
    elif kode == "p":
        jenis = "Paha"
        harga = 2000
    elif kode == "s":
        jenis = "Sayap"
        harga = 1500
    else:
        jenis = "Kode Salah"
        harga = 0

    total = harga * jumlah

    # append ke list
    orders_jenis.append(jenis)
    orders_harga.append(harga)
    orders_jumlah.append(jumlah)
    orders_total.append(total)

print()
print("".ljust(0))
print("-----------------------------------------------------------------------------------------------")
print("No.  Jenis Potong          Harga Satuan     Banyak Beli     Jumlah Harga")
print("-----------------------------------------------------------------------------------------------")
for idx in range(len(orders_jenis)):
    no = idx + 1
    j = orders_jenis[idx]
    h = orders_harga[idx]
    q = orders_jumlah[idx]
    t = orders_total[idx]
    # tampilkan dengan formatting
    print(f"{no:<4} {j:<22} Rp. {h:<13} {q:<14} Rp. {t}")
print("-----------------------------------------------------------------------------------------------")
# Hitung total keseluruhan dari list orders_total
total_belanja = sum(orders_total)

# Ambil input pembayaran dengan handling error
try:
    bayar = int(input("Masukkan Jumlah Uang Pembayaran : Rp. "))
except ValueError:
    print("Input pembayaran tidak valid, menganggap 0")
    bayar = 0

# Hitung pajak (10%) dan total akhir
ppn_rate = 0.10
ppn = int(total_belanja * ppn_rate)
semua_total = total_belanja + ppn

print("-----------------------------------------------------------------------------------------------")
print(f"Subtotal : Rp. {total_belanja}")
print(f"Pajak 10% : Rp. {ppn}")
print(f"Total Bayar: Rp. {semua_total}")

# Hitung kembalian atau kurang
if bayar >= semua_total:
    kembali = bayar - semua_total
    print(f"Uang Bayar : Rp. {bayar}")
    print(f"Kembalian  : Rp. {kembali}")
else:
    kurang = semua_total - bayar
    print(f"Uang Bayar : Rp. {bayar}")
    print(f"Kurang     : Rp. {kurang}")
      