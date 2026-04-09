#Studi Kasus Penjualan Tiket

#Input
pembeli = input("Masukkan Nama Pembeli: ")
no_hp = input("Masukkan No. HP: ")
jurusan = input("Masukkan Jurusan [SBY/BL/LMP]: ")

#Proses
if jurusan == "SBY" or jurusan == "sby":
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL" or jurusan == "bl":
    namajurusan = "Bali"
    harga = 350000
else:
    namajurusan = "Lampung"
    harga = 500000

#Input Jumlah Beli
jumlah=int(input("Masukkan Jumlah Beli Tiket: "))

#Proses Potongan
if jumlah >= 3:
    potongan= (jumlah*harga)*0.1
else:
    potongan= 0 

total= (jumlah*harga)-potongan

#Cetak Hasil
print("------------------------------------".center(40))
print("PENJUALAN TIKET PESAWAT".center(40))
print("XYZ".center(40))
print("------------------------------------".center(40))
print("Nama Pembeli             : "+str(pembeli))
print("No. HP                   : "+str(no_hp))
print("Kode Jurusan yang dipilih: "+str(jurusan))
print("Nama Kota Tujuan         : "+str(namajurusan))
print("Harga                    : Rp.",(harga))
print("Jumlah Beli              : "+str(jumlah))
print("------------------------------------")
print("Potongan yang didapat    : Rp.",+(potongan))
print("Total Bayar  : Rp.",+(total))
ubay= int(input("Masukkan Uang Bayar: Rp."))
uangkembalian= ubay-total
print("Uang Kembalian           : Rp.",+(uangkembalian))