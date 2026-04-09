#Fungsi
#def function_name(parameters):
    #"""function_docstring"""
    #statement (s)

#Mendefinisikan fungsi
print ()
def sapa(nama):
    """Fungsi untuk menyapa seseorang dengan nama yang diberikan."""
    print("Hi, " + nama + ". Apa kabar?")

#Pemanggilan fungsi 
#Output: Hi, (nama). Apa kabar?
sapa("Raihan")

#Doctring : dokumentasi atau keterangan singkat tentang fungsi yang kita buat
print(sapa.__doc__)
print()

#Pernyataan Return 
#return [expression_list]
keluaran = sapa("Raihan")
print(keluaran)  # Output: None karena fungsi sapa tidak mengembalikan nilai apapun
print()

#Definisi Fungsi print_string
def print_string(str):
    """Menampilkan argumen string str ke layar."""
    print(str)

#Kita memanggil fungsi dengan kata kunci
print_string(str="Halo Python!")
print()

#Definisi Fungsi
def print_info(nama, usia=17):
    """Menampilkan informasi nama dan umur."""
    print("Nama:", nama)
    print("Umur:", usia)

#Memanggil fungsi 
#Outpur
#Nama: Raihan
#Umur: 18
print_info(nama="Raihan", usia=18)
print()

#Pemanggilan fungsi tidak menyediakan argumen usia
print_info(nama="Raihan") 
print()

#Definisi Fungsi
def print_info( argl, *vartuple):
    """Menampilkan argumen pertama dan semua argumen tambahan."""
    print("Outputnya adalah: ")
    print(argl)
    for var in vartuple:
        print(var)
    
#Pemanggilan Fungsi
#Satu argumen
print_info(10)
print()
#Empat argumen
print_info(10, 30, 50, 70)