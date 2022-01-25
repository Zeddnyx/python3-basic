############# OPERASI DAN MANIPULASI STRING

# Menyambungkan string

nama_pertama = "ucok"
nama_tengah = "abdul"
nama_terakhir = "udin"
# gunakan tanda ( " " )untuk menambahkan spasi/lain nya
nama_lengkap = nama_pertama + " " + nama_tengah + nama_terakhir
print (nama_lengkap)


print(" ========mengecek char/character=========")
# mengecek char atau string di string
# mengecek adakah huruf a dalam nama_lengkap jika ada akan true
a = "a"
status = a in nama_lengkap
print (a + " ada di " + nama_lengkap + " = " + str(status))

# menegcek apakah tidak ada hurup a dalam nama_lengkap
a = "a"
status = a not in nama_lengkap
print (a + " tidak ada di " + nama_lengkap + " = " + str(status))



print("=======pengulangan string=============")
#mengulang string
print ("wk"*5)
#berarti wk nya akan di kali(*) 5



print("======format string===========")
###################Format string##########################
# menggunakan format ( f )
#generic string
nama = "ucok"
f_str = f"hallo {nama}"
print (f_str)

#angka
angka = 1337.8
f_str = f"angka {angka}"
print (f_str)

#boolean
bool = True
f_str = f"{bool}"
print (f_str)

#bilangan ribuan
angka = 5000000
f_str = f"juta {angka:,} " 
# tanda koma (,) untuk membuat jeda di angka ribuan ke atas
print (f_str)

#bilangan decimal
angka = 2526.829292
f_str = f"decimal {angka:.3f}" 
#angka 3 nya bisa di ubah, tanda titik itu desimal!
print (f_str)

