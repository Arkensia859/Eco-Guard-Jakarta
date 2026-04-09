#Tugas Mandiri Pertemuan 6
#Nama: Muhammad Raihan Asyauqi
#NIM: 12250032
#Kelas: 12.1A.10

#Tugas Mandiri Nomor 2: Deret Angka 1,3,5,...,100 (Ganjil) dengan Rekursif
print("")
def deret_ganjil(n): #fungsi rekursif untuk mencetak deret ganjil
    if n > 100: #basis kondisi
        return #menghentikan rekursi jika n lebih dari 100
    print(n, end=' ') #mencetak nilai n
    deret_ganjil(n + 2) #memanggil fungsi rekursif dengan n ditambah 2
print ("Deret Angka Ganjil dari 1 sampai 100:")
deret_ganjil(1) #memulai deret ganjil dari 1
print("") 
print("========================================================================")
print("")

#Tugas Mandiri Nomor 3: Mencetak nama anda sebanyak 100 kali dengan Rekursif
def cetak_nama(n, nama): #fungsi rekursif untuk mencetak nama
    if n <= 0: #basis kondisi
        return #menghentikan rekursi jika n kurang dari atau sama dengan 0
    print(nama) #mencetak nama
    cetak_nama(n - 1, nama) #memanggil fungsi rekursif dengan n dikurangi 1
print("Mencetak nama sebanyak 100 kali:")
cetak_nama(100, "Muhammad Raihan Asyauqi") #memulai pencetakan nama sebanyak 100 kali
print("========================================================================")
print("")


