#List Index Negatif
my_list = ["p","y","t","h","o","n"]

#Output: n
print(my_list[-1])

#Output: h
print(my_list[-3])
print("===============================")
print("")

#Memotong [Slicing] List
print("Memotong [Slicing] List")
my_list = ["p","y","t","h","o","n","i","n","d","o"]

#Anggota list dari 3 s/d 5 (dari h s/d n)
print(my_list[3:6])

#Anggota list dari 4 s/d yang terakhir
print(my_list[4:])

#Anggota list dari 0 s/d 4
print(my_list[:5])

#Indeks dari belakang dari -1 s/d -4
print(my_list[-1:-5:-1])
print("===============================")
print("")

#Mengubah Anggota List 
print("Mengubah Anggota List ")

#Misal ada nilai yang salah
ganjil = [1, 3, 5, 7, 9]

#Ubah item ke 3 (indeks ke 2)
ganjil[2] = 5
print(ganjil)
print("===============================")
print("")

#Menambah Anggota List
print("Menambah Anggota List ")
ganjil = [1, 3, 5, 7]
ganjil.append(9) 
print(ganjil)
ganjil.extend([11, 13, 15])
print(ganjil)
print("")

genap = [2, 4, 6]
print(genap + [8, 10, 12])
print(['p','y'] * 2)
print("===============================")
print("")

#Menghapus Anggota List
print("Menghapus Anggota List ")
my_list = ['p','y','t','h','o','n','i','n','d','o']
my_list.remove('p')

# Output: ['y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
print(my_list)  

my_list.remove('n')
#remove hanya menghapus kemunculan pertama dari nilai yang diberikan
# Output: ['y', 't', 'h', 'o', 'n', 'i', 'd', 'o']

#Output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
#Output: []
print(my_list)
print("===============================")
print("")