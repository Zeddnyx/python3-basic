############## dan komparasi
# membuat area rentang dari angka
# +++++3-------10++++++
print ("============= DAN KOMPARASI============")
inputUser = float(input('masukan angka kurang dari 3\natau lebih besar dari 10\n: '))
 # ++++++3-----------
 # memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print (inputUser,"kurang dari 3 ",isKurangDari)

 # -----------10+++++
 # memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print (inputUser,"lebih dari 10 ",isLebihDari)

isCoreect = isKurangDari or isLebihDari
print ("data yg anda masukan :",isCoreect)
print (" ")
#membuat area iris dari angka
#------3+++++++++10--------
inputUser = float(input('masukan angka lebih dari 3\natau kurang dari 10\n: '))
 # ++++++3-----------
 # memeriksa angka kurang dari 3
isKurangDari = (inputUser > 3)
print (inputUser,"lebih dari 3 ",isKurangDari)

 # -----------10+++++
 # memeriksa angka lebih dari 10
isLebihDari = (inputUser < 10)
print (inputUser,"kurang dari 10 ",isLebihDari)

isCoreect = isKurangDari or isLebihDari 
print ("data yg anda masukan :",isCoreect)
#jikan or di ganti jadi and makan hasil yg di ambil yg false



#Latihan area iris angka
 #--------0+++++++++5---------8+++++++++11---------
print("-------------")
inputUser = float(input('\nmasukan angka lebih dari 0\nmasukan angka kurang dari 5\nmasukan angka lebih dari 8\nmasukan angka kurang dari 11\n : '))
 # memeriksa angka lebih dari 0
isLebihDari = (inputUser > 0)
print (inputUser,"lebih dari 0 ",isLebihDari)

 # memeriksa angka lebih dari 5
isKurangDari = (inputUser < 5)
print (inputUser,"kurang dari 5 ",isKurangDari)

#angka lebih dari 8
isLebihDari = (inputUser > 8)
print (inputUser,"lebih dari 8 ",isLebihDari)

#angka kurang dari 11
isKurangDari = (inputUser < 11)
print (inputUser,"kurang dari 11 ",isKurangDari)

isCoreect = isLebihDari or isLebihDari
print ("data yg anda masukan :",isCoreect)


#latihan rentang angka
print ("\n====== Latihan rentang angka")
inputUser = float(input('masukan angka kurang dari 0\nmasukan angka lebih dari 5\nmasukan angka kurang dari 8\nmasukan angka lebih dari 11 :\n'))
 # memeriksa angka lebih dari 0
isKurangDari = (inputUser < 0)
print (inputUser,"kurang dari 0 ",isKurangDari)

 # memeriksa angka lebih dari 5
isLebihDari = (inputUser > 5)
print (inputUser,"lebih dari 5 ",isLebihDari)

#angka lebih dari 8
isKurangDari = (inputUser < 8)
print (inputUser,"kurang dari 8 ",isKurangDari)

#angka kurang dari 11
isLebihDari = (inputUser > 11)
print (inputUser,"lebih dari 11 ",isLebihDari)

isCoreect = isLebihDari or isLebihDari
print ("data yg anda masukan :",isCoreect)
