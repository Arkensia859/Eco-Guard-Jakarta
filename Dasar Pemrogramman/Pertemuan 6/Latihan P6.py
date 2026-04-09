list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]

#input
print("")
print ("==Masukkan Data Mahasiswa==")
ulang= int(input("Jumlah Mahasiswa :"))
for i in range(ulang):
    print ("data Ke- " + str(i+1))
    list_nim.append(input("Masukkan Nim anda : "))
    list_uts.append(int(input("Masukkan Nilai UTS anda :")))
    list_uas.append(int(input("Masukkan Nilai UAS : ")))

#proses
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

# tambah keterangan lulus/tidak dan rata-rata kelas
nl = 80  # sesuaikan ambang kelulusan jika perlu
list_status = []
for avg in list_total:
    list_status.append("Lulus" if avg >= nl else "Tidak Lulus")

#Cetak
print("=============================================================")
print("NIM\tNilai UTS\tNilai UAS\tRata-rata\tKeterangan")
print("=============================================================")
for i in range(ulang):
    print ("%s\t%i\t\t%i\t\t%.2f\t\t%s" % (list_nim[i], list_uts[i], list_uas[i], list_total[i], list_status[i]))
print("=============================================================")

# hitung jumlah lulus dan tidak lulus
passed_count = sum(1 for s in list_status if s == "Lulus")
failed_count = len(list_status) - passed_count

print("Jumlah siswa Lulus: {}".format(passed_count))
print("Jumlah siswa Tidak Lulus: {}".format(failed_count))
print("")