# Definisi Harga
HARGA = {
    'D': {'jenis': 'Dada', 'harga': 2500},
    'P': {'jenis': 'Paha', 'harga': 2000},
    'S': {'jenis': 'Sayap', 'harga': 1500}
}

# --- Bagian Masukan (Layar Masukkan) ---

print("=============================")
print("  GEROBAK FRIED CHICKEN")
print("=============================")
print("Kode JenisPotong Harga")
print("D    Dada       Rp. 2500")
print("P    Paha       Rp. 2000")
print("S    Sayap      Rp. 1500")
print("-----------------------------")

# List untuk menyimpan detail pesanan
pesanan = []
total_sebelum_pajak = 0

# Menggunakan perulangan WHILE untuk input Banyak Jenis
while True:
    try:
        # Masukan Banyak Jenis
        banyak_jenis = int(input("Banyak Jenis (item berbeda): "))
        if banyak_jenis > 0:
            break
        else:
            print("Jumlah jenis harus lebih dari 0. Coba lagi.")
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka.")

# Menggunakan perulangan FOR i in range untuk iterasi Jenis Ke-
# Proses berulang tergantung Banyak Jenis
for i in range(banyak_jenis):
    print(f"\n--- Jenis Ke - {i + 1} ---")
    
    # Perulangan WHILE untuk validasi Kode Potong [D/P/S]
    while True:
        # Masukan Kode Potong
        kode_potong = input("Kode Potong [D/P/S]: ").upper()
        
        # Menggunakan IF ELSE untuk memproses dan validasi kode
        if kode_potong in HARGA:
            
            # Perulangan WHILE untuk validasi Banyak Potong
            while True:
                try:
                    # Masukan Banyak Potong
                    banyak_potong = int(input("Banyak Potong: "))
                    if banyak_potong > 0:
                        break
                    else:
                        print("Jumlah potongan harus lebih dari 0. Coba lagi.")
                except ValueError:
                    print("Masukan tidak valid. Harap masukkan angka.")
            
            # Hitung Jumlah Harga untuk jenis ini
            harga_satuan = HARGA[kode_potong]['harga']
            jumlah_harga = harga_satuan * banyak_potong
            total_sebelum_pajak += jumlah_harga
            
            # Simpan data pesanan
            pesanan.append({
                'no': i + 1,
                'jenis_potong': HARGA[kode_potong]['jenis'],
                'harga_satuan': harga_satuan,
                'bayak_beli': banyak_potong,
                'jumlah_harga': jumlah_harga
            })
            
            break # Keluar dari perulangan validasi kode
        else:
            print("Kode tidak valid. Harap masukkan D, P, atau S.")

# --- Bagian Keluaran (Layar Keluaran) ---

print("\n\n========================================================")
print("             GEROBAK FRIED CHICHEN")
print("========================================================")
print("No. Jenis    Harga    Bayak   Jumlah")
print("    Potong   Satuan   Beli    Harga")
print("--------------------------------------------------------")

# Tampilkan detail pesanan menggunakan perulangan FOR
for item in pesanan:
    print(f"{item['no']:<3} {item['jenis_potong']:<8} Rp. {item['harga_satuan']:<7,} {item['bayak_beli']:<6} Rp. {item['jumlah_harga']:<}")

print("--------------------------------------------------------")

# Hitung dan tampilkan total pembayaran
pajak = total_sebelum_pajak * 0.10
total_bayar = total_sebelum_pajak + pajak

print(f"Jumlah Bayar Rp. {total_sebelum_pajak:,.0f}")
print(f"Pajak 10%  Rp. {pajak:,.0f}")
print(f"Total Bayar Rp. {total_bayar:,.0f}")
print("========================================================")