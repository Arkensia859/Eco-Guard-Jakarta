#Menentukan Bilangan Prima antara 1 sampai 200 (While)
#Nama: Muhammad Raihan Asyauqi
#NIM: 12250032
#Kelas: 12.1A.10
#Program Studi:Informatika

#While Looping
print("")
print("Bilangan Prima antara 1 sampai 200 adalah :") #Cetak Bilangan Prima antara 1 sampai 200 adalah :

i = 2 #Bilangan pertama yang akan diperiksa
while i <= 200: #Bilangan terakhir yang akan diperiksa
    j = 2 #Pembagi awal
    isPrima = True #Asumsi awal bilangan prima
    while j <= (i // 2): #Cek pembagi hingga setengah dari bilangan
        if i % j == 0: #Jika habis dibagi
            isPrima = False #Bukan bilangan prima
            break #Keluar dari loop pembagi
        j += 1 #Cek pembagi berikutnya
    if isPrima: #Jika bilangan prima, cetak
        print(i, end=" ") #Cetak bilangan prima
    i += 1 #Cek bilangan berikutnya
print("Terimakasih telah menggunakan program ini.") #Cetak Terimakasih  telah menggunakan program ini
print("")