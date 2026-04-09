print("Percabangan (if-else)".center(40))
print("====================================".center(40))

angka = 5
print(F"Angka yang anda masukkan adalah {angka}")
if angka > 0:
    print(angka,"adalah bilangan positif.")
print("")

print("====================================")
angka= int(input("Masukkan angka: "))
if angka >= 0:
    print(angka,"adalah bilangan positif.")
else:
    print(angka,"adalah bilangan negatif.")
print("")
print("====================================")

kode_baju= input("Masukkan Kode Baju [SP/AD]: ")
ukuran= input("Masukkan Ukuran Baju [S/M]: ")
print("")

if kode_baju == "SP" or kode_baju == "sp":
   merk = "SuperDry"
   if ukuran == "S" or ukuran == "s":
       harga = 450000
   elif ukuran == "M" or ukuran == "m":
       harga = 500000
   else:
       harga = 0
elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
         harga = 650000
    elif ukuran == "M" or ukuran == "m":
         harga = 700000
    else:
         harga = 0
else:
    merk = "Anda Salah Input Kode Merk"
    harga = 0
print("")
print("====================================")
print("Merk Baju: "+str(merk))
print("Harga Baju: Rp.",(harga))