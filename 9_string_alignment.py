###############STRING  Aligenmnt

print("=============string multi line")
#string multiline
data_n = "ucok"
data_as = "LA"
data_str = f"""nama = {data_n} 
asal = {data_as}
 """
print (data_str)

######################LATIHAN DATETIME########################
print ("================ date and time")
import datetime 

hari = datetime.date.today()
print (hari)

print ("\nSilahkan isi data di bawah ini")

tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

tanggal_lahir = (tanggal,bulan,tahun)
print (f"tanggal lahir anda : ",tanggal_lahir)


#data anda
print ("="  * 10,"Data lengkap\n")
print (f"nama : {data_n} ")
print (f"alamat : {data_as}")
print (f"tangga lahir : {tanggal_lahir}")

