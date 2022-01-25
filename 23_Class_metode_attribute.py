
#harus hurup kapital di awal jika ingin menulis 2 kata
           
class HargaBaju:
      
      def __init__(self,merek,harga):
            self.merek = merek
            self.harga = harga
            
barang1 = HargaBaju(merek = 'gucci', harga = 500)

print (barang1.merek) # akan mencetak nilai yg ada di harga1
print (barang1.harga)


print("")
#bisa juga seperti ini
barang2 = HargaBaju('dior',400)

print(barang2.merek)
print(barang2.harga)



print("")

# bisa juga menggunakan metode seperti di bawah
class HargaMobil:
      
      def __init__(self,brand,price):
            self.brand = brand
            self.price = price
            self.garansi = '1 tahun'
            self.power = 'listrik'
            
mobil1 = HargaMobil('Tesla',9999)
 
print("Brand :",mobil1.brand)
print("Price :",mobil1.price)
print("garansi :",mobil1.garansi)
print("Tenaga :",mobil1.power)
