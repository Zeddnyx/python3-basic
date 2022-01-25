#OPERASI KOMPARASI
#setiap hasil dari operasi komparasi itu boolean
# >,<,>=,<=,==,!=,is,is not
print ("===========OPERASI KOMPARASI=============")

a = 5
b = 4

#lebih besar dari (>)
print ("=== lebih besar dari (>)===")
hasil = a > b
print (a, '>' ,b, "=", hasil)
hasil = b > a
print (b, '>' ,a, "=", hasil)
hasil = b > b
print (b, '>' ,b, "=", hasil)


#lebih dari sama dengan (>=)
print ("\n==== lebih besar dari sama dengan (>=)")
hasil = a >= b
print (a, '>=' ,b, "=", hasil)
hasil = b >= a
print (b, '>=' ,a, "=", hasil)
hasil = b >= b
print (b, '>=' ,b, "=", hasil)
print("hasil yg nilai sama akan true")



#kurang dari sama dengan (<=)
print ("\n==== kurang besar dari sama dengan (<=)")
hasil = a <= b
print (a, '<=' ,b, "=", hasil)
hasil = b <= a
print (b, '<=' ,a, "=", hasil)
hasil = b <= b
print (b, '<=' ,b, "=", hasil) 
print("akan true jika nilai sama")


# sama dengan (==)
print ("\n==== sama dengan (==)")
hasil = a == b  
print (a, '==' ,b, "=", hasil)
hasil = b == a
print (b, '==' ,a, "=", hasil) 
hasil = b == b
print (b, '==' ,b, "=", hasil) 
print("akan true jika nilai sama")


# tidak sama dengan (!=)
print ("\n==== tidak sama dengan (!=)")
hasil = a != b
print (a, '!=' ,b, "=", hasil) 
hasil = b != a
print (b, '!=' ,a, "=", hasil)
hasil = b != b
print (b, '!=' ,b, "=", hasil) 
print("akan True jika nilai tidak sama")


# 'is', komparasi object (is)
x = 5
y = 5

print ("\n====komparasi object (is)")
hasil = x is y
print (x, 'is' ,y, "=", hasil)

x = 5
y = 6
hasil = x is y
print (x, 'is' ,y,'=',hasil)
print("akan true jika object sama")


# komparasi object (is not)
print ("\n====komparasi object (is not)")
x = 5
y = 5
hasil = x is not y
print (x, 'is not' ,y, "=", hasil)

x = 5
y = 6
hasil = x is not y
print (x, 'is not' ,y, "=",hasil)

print ("akan true jika object tidak sama")