################## OPERASI NOT,OR,AND,XOR(^)
print ("========OPERASI  NOT,OR,AND,XOR=========")
#NOT
print ("====== OPERASI NOT")
print ("hanya bernilai boolean")
a = True
b = not a
print ("data a =",a)
print ("data b =",b)



#OR (jika salah satu True makan hasilnya True)
a = True
b = False
c = a or b
print ("-----------------OR")
print (a , " OR",b, "=" ,c)
a = False
b = False
c = a or b
print (a , "OR",b, "=" ,c)
a = False
b = True
c = a or b
print (a , "OR",b, " =" ,c)
a = True
b = True
c = a or b
print (a , " OR",b, " =" ,c) 
print("OR (jika salah satu True makan hasilnya True) ")




a = True
b = False
c = a and b
print ("\n-----------------AND")
print (a , " AND",b, "=" ,c)
a = False
b = False
c = a and b
print (a , "AND",b, "=" ,c)
a = False
b = True
c = a and b
print (a , "AND",b, " =" ,c)
a = True
b = True
c = a and b
print (a , " AND",b, " =" ,c)
print(r'''jika false and false = false 
false and true = false
jika true and true = true
''')



a = True
b = False
c = a ^ b
print ("-----------------XOR")
print (a , " XOR",b, "=" ,c)
a = False
b = False
c = a ^ b
print (a , "XOR",b, "=" ,c)
a = False
b = True
c = a ^ b
print (a , "XOR",b, " =" ,c)
a = True
b = True
c = a ^ b
print (a , " XOR",b, " =" ,c)
print("XOR (akan true jika salah satu true, akan false jika ada 2 nilai true)")