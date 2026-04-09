#Latihan
#Studi Kasus : Pendaftaran Mahasiswa Baru

# Input Data Diri
print("===Pendaftaran Mahasiswa Baru===".center(50))
print("Silahkan isi data diri anda dengan benar".center(50))
print("")
nama = input("Masukkan Nama Anda : ")
nis = input("Masukkan NIS Anda : ")
jurusan = input("Masukkan Jurusan Anda (SI/SIA) : ")

#Proses
if jurusan == "SI" or jurusan == "si":
    jurusan = "Sistem Informasi"
    harga = 2400000
elif jurusan == "SIA" or jurusan == "sia":
    jurusan = "Sistem Informasi Akuntansi"
    harga = 2000000
else:
    jurusan = "Anda Salah Input Jurusan"
    harga = 0
print("")

#Cetak Hasil
print("=============================================".center(50))
print("===Pendaftaran Mahasiswa Baru===".center(50))
print("=============================================".center(50))
print("Nama Anda : " + str(nama))
print("NIS Anda : " + str(nis))
print("Jurusan Anda : " + str(jurusan))
print("Biaya Pendaftaran : Rp.", (harga))
print("============================================================")
bayar = int(input("Masukkan Uang Bayar : Rp."))

if bayar >= harga:
    print("Uang Anda Cukup Untuk Membayar Biaya Pendaftaran")
    kembalian = bayar - harga
    print("Uang Kembalian Anda : Rp." + str(kembalian))
    print("Terimakasih", nama, "Telah Mendaftar")
    print("")
elif bayar < harga:
    kurang = harga - bayar
    print("Maaf", nama, "Jumlah Uang Anda Tidak Cukup, Silahkan Tambah Uang Anda Sebesar : Rp." + str(kurang))
    print("")
    lanjut = input("Apakah Anda Ingin Melanjutkan Pendaftaran? (Y/N) : ")
    if lanjut == "Y" or lanjut == "y":
            print("Mohon Tambahkan Uang Anda Minimal Sebesar : Rp." + str(kurang))
            bayar = int(input("Masukan Uang Tambahan Anda : Rp."))
            total_bayar = bayar + kurang
            if total_bayar == harga:
                print("")
                print("Uang Kembalian Anda : Rp.0")
                print("Terimakasih", nama, "Telah Mendaftar")
                print("")
            elif total_bayar > harga:
                kembalian = total_bayar - harga
                print("")
                print("Jumlah Uang Anda Cukup Untuk Membayar Biaya Pendaftaran")
                print("Uang Kembalian Anda : Rp." + str(kembalian))
                print("Terimakasih", nama, "Telah Mendaftar")
                print("")
            else:
                print("")
                print("Input Tidak Valid, Pendaftaran Dibatalkan")
                print("Mohon Mendaftar Ulang, Terimakasih")
                print("")
    elif lanjut == "N" or lanjut == "n":
        print("Pendaftaran Dibatalkan, Terimakasih")
        print("")
    else:
        print("")
        print("Input Tidak Valid, Pendaftaran Dibatalkan")
        print("Mohon Mendaftar Ulang, Terimakasih")
        print("")
else:
    print("")
    print("Input Tidak Valid, Pendaftaran Dibatalkan")
    print("Mohon Mendaftar Ulang, Terimakasih")
    print("")