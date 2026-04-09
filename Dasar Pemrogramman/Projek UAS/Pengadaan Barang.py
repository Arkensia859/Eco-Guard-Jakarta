'''
Universitas Nusa Mandiri
Program Studi Teknik Informatika
Kelas: 12.1A.10 
Mata kuliah: Dasar Pemrogramman

Kelompok 6 : PROGRAM PEMINJAMAN BUKU PERPUSTAKAAN TK 
Anggota Kelompok:
1. Muhammad Raihan Asyauqi (12250032)
2. Moses Christian Lumbantobing (12250093)
3. Agata Hoogeveen Farra (12259057)
'''
#Mengimport Waktu 
import datetime

# lama pinjam default (hari)
loan_period_days = 3

# List Buku di Perpustakaan TK Tadika Mesra
buku = [
    {"id": 1, "judul": "Belajar Huruf A-Z", "jumlah": 3},
    {"id": 2, "judul": "Cerita Pendek", "jumlah": 2},
    {"id": 3, "judul": "Mengenal Angka", "jumlah": 4},
    {"id": 4, "judul": "Dongeng Anak", "jumlah": 1},
    {"id": 5, "judul": "Calistung", "jumlah": 4}
]

peminjaman = []
riwayat_pengembalian = []

# Fungsi untuk menampilkan daftar buku
def tampilkan_buku():
    print("\nDaftar Buku di Perpustakaan:")
    print("ID | Judul Buku                 | Jumlah | Status")
    print("---------------------------------------------------")
    for b in buku:
        status = "Tersedia" if b["jumlah"] > 0 else "Habis"
        print(f"{b['id']:2} | {b['judul']:<25} | {b['jumlah']:6} | {status}")
    print()

# Fungsi untuk meminjam buku
def pinjam_buku():
    nama = input("\nNama anak: ").strip()
    try:
        id_buku = int(input("Masukkan ID buku yang ingin dipinjam: "))
    except ValueError:
        print("ID tidak valid.\n")
        return

    try:
        qty = int(input("Jumlah buku yang ingin dipinjam: "))
        if qty <= 0:
            print("Jumlah harus lebih dari 0.\n")
            return
    except ValueError:
        print("Jumlah tidak valid.\n")
        return

    for b in buku:
        if b["id"] == id_buku:
            if b.get("jumlah", 0) >= qty:
                b["jumlah"] -= qty
                now = datetime.datetime.now()
                due = now + datetime.timedelta(days=loan_period_days)
                # simpan jumlah yang dipinjam di record peminjaman + waktu pinjam + jatuh tempo
                peminjaman.append({
                    "nama": nama,
                    "judul": b["judul"],
                    "id": b["id"],
                    "jumlah": qty,
                    "tgl_pinjam": now.strftime("%Y-%m-%d %H:%M:%S"),
                    "tgl_jatuh_tempo": due.strftime("%Y-%m-%d")
                })
                print()
                print(f"Buku '{b['judul']}' sebanyak {qty} buah berhasil dipinjam oleh {nama} pada {now.strftime('%Y-%m-%d %H:%M:%S')}.")
                print(f"Harus dikembalikan sebelum: {due.strftime('%Y-%m-%d')}\n")
                return
            else:
                print(f"Maaf, stok buku tersebut tidak cukup. Hanya tersedia {b.get('jumlah',0)} buah.\n")
                return
    print("ID buku yang anda masukkan tidak ditemukan.\n")

# Fungsi untuk mengembalikan buku
def kembalikan_buku():
    nama = input("\nNama anak: ").strip()
    judul = input("Judul buku yang dikembalikan: ").strip()
    try:
        qty = int(input("Jumlah buku yang dikembalikan: "))
        if qty <= 0:
            print("Jumlah harus lebih dari 0.\n")
            return
    except ValueError:
        print("Jumlah tidak valid.\n")
        return

    # cari record peminjaman yang cocok (by nama + judul)
    for p in list(peminjaman):  # iterate over copy to allow removal
        if p["nama"].lower() == nama.lower() and p["judul"].lower() == judul.lower():
            if qty > p["jumlah"]:
                print(f"Anda mengembalikan lebih banyak dari yang dipinjam ({p['jumlah']} buah).\n")
                return
            # tambahkan kembali stok pada data buku berdasarkan id
            for b in buku:
                if b["id"] == p.get("id"):
                    b["jumlah"] = b.get("jumlah", 0) + qty
                    break
            now = datetime.datetime.now()
            # catat ke riwayat pengembalian
            riwayat_pengembalian.append({
                "nama": nama,
                "judul": judul,
                "id": p.get("id"),
                "jumlah_kembali": qty,
                "tgl_pinjam": p.get("tgl_pinjam"),
                "tgl_kembali": now.strftime("%Y-%m-%d %H:%M:%S")
            })
            # kurangi/ hapus record peminjaman sesuai jumlah yang dikembalikan
            if qty == p["jumlah"]:
                peminjaman.remove(p)
            else:
                p["jumlah"] -= qty
            print(f"Buku '{judul}' sebanyak {qty} buah berhasil dikembalikan oleh {nama} pada {now.strftime('%Y-%m-%d %H:%M:%S')}.\n")
            return

    print("Data peminjaman tidak ditemukan.\n")

# Fungsi untuk melihat daftar peminjaman
def lihat_peminjaman():
    print("\nDaftar Peminjaman:")
    if not peminjaman:
        print("Belum ada peminjaman.\n")
    else:
        now = datetime.datetime.now()
        for p in peminjaman:
            # status jatuh tempo
            try:
                due_dt = datetime.datetime.strptime(p.get("tgl_jatuh_tempo"), "%Y-%m-%d")
                overdue = now > due_dt
                status = "Telat" if overdue else "Tepat Waktu"
            except Exception:
                status = "Unknown"
            print(f"- {p['nama']} meminjam Buku '{p['judul']}' (Jumlah: {p['jumlah']})")
            print(f"  Tgl pinjam : {p.get('tgl_pinjam')}")
            print(f"  Jatuh tempo: {p.get('tgl_jatuh_tempo')}  Status: {status}")
        print()

# Fungsi untuk melihat riwayat pengembalian
def lihat_riwayat():
    print("\nRiwayat Pengembalian:")
    if not riwayat_pengembalian:
        print("Belum ada riwayat pengembalian.\n")
    else:
        for r in riwayat_pengembalian:
            print(f"- {r['nama']} mengembalikan Buku '{r['judul']}' (Jumlah: {r['jumlah_kembali']}) | Pinjam: {r.get('tgl_pinjam')} | Kembali: {r.get('tgl_kembali')}")
        print()

# Menu utama
def menu():
    while True:
        print("\n=== Program Peminjaman Buku TK Tadika Mesra ===")
        print("1. Lihat Daftar Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Lihat Peminjaman")
        print("5. Lihat Riwayat Pengembalian")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()
        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tampilkan_buku()
            pinjam_buku()
        elif pilihan == "3":
            kembalikan_buku()
        elif pilihan == "4":
            lihat_peminjaman()
        elif pilihan == "5":
            lihat_riwayat()
        elif pilihan == "6":
            print("Keluar program.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu()