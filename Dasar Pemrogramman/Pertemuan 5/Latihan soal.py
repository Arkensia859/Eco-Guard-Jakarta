ulang = 2
for i in range(ulang):
    print("data ke-" + str(i+1))
    nama= input("Masukkan Nim anda : ")
    uts = int(input("Masukkan Nilai UTS anda : "))
    uas = int(input("Masukkan Nilai UAS : "))
    print("NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama, uts, uas))
    print("-------------------------------------\n")
