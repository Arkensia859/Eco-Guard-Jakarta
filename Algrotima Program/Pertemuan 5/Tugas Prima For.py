#Menentukan Bilangan Prima antara 1 sampai 200 (For)
#Nama: Muhammad Raihan Asyauqi
#NIM: 12250032
#Kelas: 12.1A.10
#Program Studi:Informatika
 
#For Looping
print("")
print("Bilangan Prima antara 1 sampai 200 adalah :") #Cetak Bilangan Prima antara 1 sampai 200 adalah :

for i in range(2, 201): #Periksa bilangan dari 2 hingga 200
    isPrima = True #Asumsi awal bilangan prima
    for j in range(2, (i // 2) + 1): #Cek pembagi hingga setengah dari bilangan
        if i % j == 0: #Jika i habis dibagi j
            isPrima = False #Bukan bilangan prima
            break #Keluar dari loop pembagi
    if isPrima: #Jika bilangan prima, cetak
        print(i, end=" ") #Cetak bilangan prima
print("Terimakasih telah menggunakan program ini.") #Cetak Terimakasih  telah menggunakan program ini