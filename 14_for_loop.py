##################### LOOPING

# for kondisi:
#      aksi
print("================looping")
angka2 = [1,3,5,7,8] # akan menjadi list sesuai no yg di ketik
for i in angka2:
  print (f"i sekarang menjadi {i}")
print ("end\n")

print("loop range (no berurutan")
# range
angka_range = range (5) # akan menjadi no yg berurutan 1-5
for i in range(5):
   print (f"i sekarang menjadi {i}")
print ('end\n')

print("range 1.5 ( not flaot tapi angka aka berurutan)")
angka_range = range (1,5) # 1,5 bukan float tapi akan memulai dari angka 1
for i in range(5):
   print (f"i sekarang menjadi {i}")
print ('end\n')

print("============== loop string")
# menggunakan string
data_str = "hallo brooo"
for data_str in data_str:
  print (data_str)
  
  
 #loop
 
for gweh in range(0,5): #gweh adalah variable dari range!
  print("nbeee")
  
  
#contoh 

ulangi = int(input("mau berapa kali di ulang? :"))
for i in range(0,ulangi):
      print("owoooooh")
