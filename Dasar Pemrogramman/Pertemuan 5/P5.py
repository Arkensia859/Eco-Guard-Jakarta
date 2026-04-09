numbers = [7,5,9,8,9,0,8,4,0,]

sum = 0

for each in numbers:
    sum = sum + each

print("Jumlah Semuanya : ", sum)
print("")
print("===============================")

mapel=["Matematika","Fisika","Kimia"]
for i in range (len (mapel)):
    print("Saya suka", mapel [i])
print("")
print("===============================")

count = 0
while count < 5:
    print("Nilai count adalah :", count)
    count = count + 1
print("Goodbye!")
print("")
print("===============================")

for letter in 'PythonProgramming':
    if letter == "g":
        break
    print('Huruf saat ini :', letter)
print("Goodbye!")
print("")
print("===============================")

count = 0
while count < 8:
    print(count, "kurang dari 8")
    count = count + 1
else:
    print(count, "tidak kurang dari 8")
print("Goodbye!")
print("")
print("===============================")