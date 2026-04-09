#PROGRAM HITUNG GAJI KARYAWAN

#Input Data Karyawan
print("")
print("===Program Hitung Gaji Karyawan===".center(50))
print("Silahkan isi data diri anda dengan benar".center(50))
print("")
nama = input("Masukkan Nama Karyawan : ")
jabatan = input("Masukkan Jabatan Anda (1/2/3) : ")
pendidikan = input("Masukkan Pendidikan Terakhir Anda (SMA/D1/D3/S1) : ")
jam_kerja = int(input("Masukkan Jumlah Jam Kerja Anda (Jam) : "))
print("")

#Proses Hitung Gaji
if jabatan == "1":
    tunjangan_jabatan = 0.05 * 3000000
elif jabatan == "2":
    tunjangan_jabatan = 0.1 * 3000000
elif jabatan == "3":
    tunjangan_jabatan = 0.15 * 3000000
else:
    tunjangan_jabatan = 0
    print("Maaf Tidak Ada Golongan Jabatan Anda")

#Hitung Tunjangan Pendidikan
if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = 0.025 * 3000000
elif pendidikan == "D1" or pendidikan == "d1":
    tunjangan_pendidikan = 0.05 * 3000000
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = 0.2 * 3000000
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan = 0.3 * 3000000
else:
    tunjangan_pendidikan = 0
    print("Maaf Tidak Ada Tunjangan Pendidikan Anda")

#Hitung Gaji Pokok
gaji_pokok = 3000000

#Hitung Gaji Lembur
if jam_kerja > 8:
    jam_lembur = jam_kerja - 8
    gaji_lembur = jam_lembur * 35000
else:
    gaji_lembur = 0

#Hitung Total Gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + gaji_lembur

print("===============================================")
print("")

#Cetak Hasil
print("Karyawan yang bernama     " + str(nama))
print("Honor yang diterima ")
print("     Tunjangan Jabatan          Rp." + str(int(tunjangan_jabatan)))
print("     Tunjangan Pendidikan       Rp." + str(int(tunjangan_pendidikan)))
print("     Honor Lembur               Rp." + str(int(gaji_lembur)))
print("                                             __________+")
print("     Total Gaji                              Rp." + str(int(total_gaji)))
print("(Gaji Pokok + Tunjangan + Lembur)")
print("")
