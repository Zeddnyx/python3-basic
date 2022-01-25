print(r"""
1.( * )
2.( + )
""")
nanya = "y"
while nanya == "y" :
      
      kalkulator = input("[*] Pilih: ")

      if kalkulator == "1":
           user = int(input("[*] Masukan angka "))
           user1 = int(input("[*] Masukan angka "))
           hasil = user * user1
       
           print("[*] hasil ", user,"*",user1,"=", hasil )
           break
      
      if kalkulator == "1":
           user = int(input("[+] Masukan angka "))
           user1 = int(input("[+] Masukan angka "))
           hasil = user + user1
          
           print("[+] hasil ",user,"+",user1,"=", hasil )
           break
       
      else:
           print(" ")
          
           
      nanya = input("mau coba lagi (y/n)? :")
      if nanya != "y":
            break

      
print('selesai')