##################  EXCEPTION HANDLING 
''' jenis2 kesalahan yg di kenali python '''

#x = 10

#hasil = x / 0  # 10 tidak bisa di bagi 0 karena melanggar hukum matematika
#print (hasil)
# pasti akan muncul error zero divison


 #kita coba menggunakan try except 
 #guna nya untuk melanjutkan jika ada code error
'''
x = 10

try:
  hasil = x / 0 # jika 0 di ganti dengan angka lain maka tulisan ada error tidak akan muncul 
  print (hasil)
  
except:
  print ("[*]ada error")

print('program selesai')
'''


try:
  x = int(input("masukan angka lebih besar dari 0 "))
  assert x > 0
  #hasil yg kita input akan menjadi variabel x Contoh masukan
  #angka 5 nah angka 5 > 0 = benar 
except:
  print ("errrorrrrrrr!")
else:
  print ("benarrr")

print ("")

print("======== try except")
try:
  x = int(input("masukan bilangan genap "))
  assert x % 2 == 0
except:
  print ("[*] bukan bilangan genap")
else:
  print ("[*] benar itu bilangan genap")
  # assert itu hanya bernilai True and False
  
