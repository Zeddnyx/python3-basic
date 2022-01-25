#prioritas operasi

x = 4
y = 3
z = 2
'''
urutan prioritas 
 1. ()
 2. exponen **
 3. perkalian dkk * / ** % //
 4. pertambahan dan pengurangan + -
 '''
hasil = x ** y * z + x / y - y // z 
print ( x, '**' ,y, '*' ,z, '+' ,x, '/' ,y, '-' ,y, '//' ,z, '=' ,hasil )

hasil = x + y * z
print (x, '+' ,y,'*' ,z, '=' ,hasil)

# () akan mengambil langkah pertama, seperti contoh yg sudah sya urutkan
hasil = (x + y) * z
print ('(',x, '+' ,y,') *' ,z, '=' ,hasil)
print (" ")