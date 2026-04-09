print()
print('Soal Nomor 1')
print()
matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]) 

#Pengisian nilai pada matriks
for i in range(4):
    for j in range(4):
        if i<=j:
            matriks[i][j]= j + 1
        if i>j:
            matriks[i][j]= 0

#Menampilkan matriks
for i in range (4):
    print(matriks[i])
print()

print("=======================================================================")

print("Soal Nomor 2")
print()
matriks2=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])

#Pengisian nilai pada matriks
for i in range(4):
    for j in range(4):
        if i>=j:
            matriks2[i][j]= i + 1
        if i<j:
            matriks2[i][j]= 0

#Menampilkan matriks
for i in range (4):
    print(matriks2[i])
print()

print("=======================================================================")

print("Soal nomor 3")
print()
matriks3=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])

#Pengisian nilai pada matriks
for i in range(4):
    for j in range(4):
        if i==j:
            matriks3[i][j]= 1
        if i<j and i>j:
            matriks3[i][j]= 0

#Menampilkan matriks
for i in range (4):
    print(matriks3[i])
print()

print("=======================================================================")

print("Soal Nomor 4")
print()
nilai = [1,2,3,4]
for i in range (len(nilai)):
    nilai[i]= 2*i+1
    print(nilai[i])
print()

print("=======================================================================")

