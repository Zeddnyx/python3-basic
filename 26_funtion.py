###################### FUNCTION ######################

def awal():
  print("haloo world")

print("akhir dari function")
awal()



# bisa juga seperti ini

def jumalh():
  hasil = 10 * 10
  print (hasil)
print ("akhir dari function")
jumalh()

# function Argument
def sambutan(nama):
  print ("hallo",nama,"u fine?")
  
print (" ")
sambutan(8181)

# funtion Argument angka
def jumlah(angka):
  hasil = angka * 10
  print ("hasil dari angka * 10 =",hasil)

jumlah(20)


# function yg mengembalikan nilai
def jumlah(angka):
  hasil = angka * 10
  return hasil

print ('hasil nya',jumlah(30))
#kunci nya return !