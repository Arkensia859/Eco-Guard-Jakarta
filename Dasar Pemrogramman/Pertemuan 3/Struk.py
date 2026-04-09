print("SDH KELAPA 2".center(40))
print("====================================".center(40))
print("Selamat Datang di Toko SDH KELAPA 2".center(40))
print("Silahkan Berbelanja Sepuasnya".center(40))
print("")
nama= input("Masukkan Nama Pembeli: ")
uang= int(input("Masukkan Uang Pembeli: Rp."))

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
print("==============================================================================")
print("")

print("")
print("================================".center(40))
print("STRUK PEMBELIAN".center(40))
print("================================".center(40))
print("")
print("SDH KELAPA 2".center(40))
print("")
print("Alamat   : JL RAYA AKSES UI")
print("Kota     : DEPOK")
print("Telp.    : 0896-4388-2100")
print("NPWP     : ")
print("")
print("...................................")
print("")

print("No.      : 00134")
print("Tgl.     : 09/21/2025    18:25:38")
print("Sales    : AFIFAH        Shift 1")
print("")
print("....................................")
print(barang1)
print(str(harga1) + " x " + str(jumlah1) + " = " + "Rp." + str(total1))
print(barang2)
print(str(harga2) + " x " + str(jumlah2) + " = " + "Rp." + str(total2))
print("")
print("....................................")
print("GRAND TOTAL  : Rp." + str(total))
print("BAYAR        : Rp." + str(uang))
print("Cash Rp." + str(uang))
print("")
print(".....................................")

print("")
if uang >= total_bayar:
    kembalian= uang-total_bayar
    print("Kembalian    : Rp." + str(kembalian))
else : 
    print ("Maaf", nama, "Jumlah Uang Anda Tidak Cukup, Silahkan Tambah Uang Anda")
print("")
print("........................................")
print("BARANG YANG SUDAH DIBELI TIDAK DAPAT DITUKAR".center(40))
print("TERIMA KASIH".center(40))
print("Info Layanan Pengiriman: ")
print("")
print("Dev.: 0812-3456-7890SDH13132250921100134") 