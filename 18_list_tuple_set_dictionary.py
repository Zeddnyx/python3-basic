###########  myList tuple set dictonary
'''
list menggunakan []
tuple menggunakan ()
set menggunakan {}
'''

####### MYLIST 
print("-------- LIST")
mylist = ["jagung",7,"kambing","rumah",True]
print(mylist)


print("\nbisa juga mengakses salah satu nilai")
print(mylist[2])

print("\nmengecek nilai")
print(0 in mylist)

print("\n mengecek angka yg terbesar")
mynumber = [1,67,7,107,97,102]
print(max(mynumber))

print("\nmenambah angka")
mynumber[2] = 33
print(mynumber)

print("\nmengurutkan no")
mynumber.sort()
print(mynumber)
# kalo string? akan mengurutkan sesuai abjad string

#operator simpel
print("\ndi kali")
myperkalian = mylist * 2#mylist di kali 3 
print(myperkalian)




#####  TUPLE
# sipat nya imotable/imortal/tidak bisa di ubah
#jika nilai yg sudah di tulis di ubah maka akan error

#sama aja kek list cuman tidak bisa mengubah data
print("\n---------TUPLE")

tuple = ("zedd","zay","ucok")
print(tuple)



##### SET
# set tidam mengurutkan object yg ada di dalamnya
# set tidak mengijinkan ada 2 nilai yg sama kalo ada akan di ambil salah satu

print("\n--------- SET")
myset = {'kamu','4','False','kambing'}
print(myset)

print("\nmenggunakan set = mengrandom ")
myset2 = set("im set") 
print(myset2)


#Tambahkan elemen dari tropicalke thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


########  DICTIONARY
#menyimpan nilai dalam suata "key value"

print("\n-------dictionary")
mydict = {
      "name": "zedd",
      "addres": "indonesia",
      "hobby": ["Study","listen music","whatch movie"]
}

print(mydict)
print(" \n")
#bisa juga seperti ini, mengambil salah satu nilai
print(mydict.get("name"))
print(" \n")
''' apa gunanya? 
jika membuat sesuatu yg ada banyak biodata nya nah kita
bisa memilih salah satu data nya'''

#mengupdate nilai
mydict["addres"] = "new zealand"
print(mydict)
print(" \n")
# dict angka
mydictNumb = {
      1: "susu",
      2: "kambing",
      3: "mobil"
}
print(mydictNumb)
print(" \n")

#jika ingin mengambil salah satu nilai
print(mydictNumb.get(1))