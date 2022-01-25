# input data 

#data yg di masukan pasti type string
data = input ("Masukan Nama: ")
print (data)


#jika ingin mengambil int maka harus di casting
data_int = int(input("Masukan angka:"))
print (data_int)


#Bagaimana jika boolean?
#nilai akan tetap true harus di casting ke int
data_bool = bool(input("Basukan Binary: "))
print (data_bool)

#float
data_float = float(input("Masukan angka (otomatis akan jadi float) : "))
print (data_float)
