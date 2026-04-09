#Tugas Pertemuan 3: Menggabungkan dari berbagai operator

#Nama: Muhammad Raihan Asyauqi
#NIM: 12250032
#Kelas: 12.1A.10
#Program Studi:Informatika

#Operasi Penugasan
print("====================================")
print("Toko Arkensia".center(40))
print("====================================")
print("Selamat Datang di Toko Arkensia".center(40))
print("Silahkan Berbelanja Sepuasnya".center(40))
print("")
nama= input("Masukkan Nama Pembeli: ")
uang= int(input("Masukkan Uang Pembeli: Rp."))
print ("====================================")

barang1= input("Masukkan Nama Barang 1: ")
harga1= int(input("Masukkan Harga Barang 1: Rp."))
jumlah1= int(input("Masukkan Jumlah Barang 1: "))
barang2= input("Masukkan Nama Barang 2: ")
harga2= int(input("Masukkan Harga Barang 2: Rp."))
jumlah2= int(input("Masukkan Jumlah Barang 2: "))
print("======================================")

print("")
#Operasi Aritmatika
total1= harga1*jumlah1
total2= harga2*jumlah2
total= total1+total2
print ("Total Harga Pembelian Anda adalah sebesar: Rp."+ str(total))

print("")
#Operasi Perbandingan & Logika
if total >= 50000: 
    print ("Selamat", nama, "Anda Mendapatkan Diskon 10%")
    diskon= total*0.1
    total_bayar= total-diskon
    print("Total Harga Pembelian Anda Jadi Sebesar: Rp."+ str(total_bayar))
else : 
    total_bayar= total

if uang >= total_bayar:
    print ("Jumlah Uang Anda Cukup Untuk Membayar Perbelanjaan Anda")
    kembalian= uang-total_bayar
    print ("Terimakasih", nama, "Telah Berbelanja Disini, Uang Kembalian Anda: Rp."+ str(kembalian))
else : 
    print ("Maaf", nama, "Jumlah Uang Anda Tidak Cukup, Silahkan Tambah Uang Anda")
print("")

