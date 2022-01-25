## QUEUE AND STACK

#Stack (tumpukan)
print("--"*10,"Stack")
hp = []
hp.append ("vivo")

print ("hp saat ini: ",hp)

print("")
hp.append("redmi")
hp.append("samsung")
hp.append("oddo")
hp.append("iphone")

print ("hp yg tersedia saat ini :",hp)
print ("")

# pop (akan menghapus)
print("--"*10,"pop (menghapus)")
hp.pop()
print ("hp yg tersedia saat ini :",hp)
print(" \n")


#queue
from collections import deque
print ("antrian PMB")

calonMS = deque([])
calonMS.append("ujang")

print ("calon mahasiswa :",calonMS)

calonMS.append("ucok")
calonMS.append("ucup")
calonMS.append("udin")

print ("antrian mahasiswa saat ini :",calonMS)

calonMS.popleft() #akan menghapus list dari yg pertama
print ("antrian mahasiswa yg keluar :",calonMS)