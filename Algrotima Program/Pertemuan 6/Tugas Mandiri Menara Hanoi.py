#Tugas Mandiri Pertemuan 6
#Nama: Muhammad Raihan Asyauqi
#NIM: 12250032
#Kelas: 12.1A.10

print("")
#Tugas Mandiri Nomor 1: Gambarlah Menara Hanoi dengan 3  piringan, lalu membuat algoritma pemindahan piringan tersebut ke menara tujuan menggunakan rekursif
def hanoi(n, sumber, tujuan, bantu): #fungsi rekursif untuk memindahkan piringan
    if n == 1: #basis kondisi
        print(f"Pindahkan piringan 1 dari {sumber} ke {tujuan}") #memindahkan piringan tunggal
        return
    hanoi(n - 1, sumber, bantu, tujuan) #memindahkan n-1 piringan ke tiang bantu
    print(f"Pindahkan piringan {n} dari {sumber} ke {tujuan}") #memindahkan piringan terbesar ke tiang tujuan
    hanoi(n - 1, bantu, tujuan, sumber) #memindahkan n-1 piringan dari tiang bantu ke tiang tujuan

#Jumlah Piringan
jumlah_piringan = 3
print(f"Gambarlah Menara Hanoi dengan {jumlah_piringan} piringan:")
hanoi(jumlah_piringan, 'A', 'C', 'B') #memulai pemindahan piringan dari tiang A ke tiang C dengan tiang B sebagai bantu
