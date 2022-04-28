 # class
# source sekolah koding oop python3

print('# class')
class Player:
	nama = 'messi'

	#untuk menampikan nama
	def get_name(self):
		return self.nama

pemain = Player()
print(pemain.nama)

#bisa juga seperti ini
print(pemain.get_name())




## metode paramaeter
print('\n# metode parameter')
class Play:

	def get_nama(self, nama):
		self.nama = nama
		return self.nama

player1 = Play()
print(player1.get_nama('icok'))

player2 = Play()
print(player2.get_nama('udin'))




## class metode init
print('\n# metode init')
class Player2:
	def __init__(self, nama, age):
		self.nama = nama
		self.age = age

	def get_nama(self):
		return self.nama

	def get_age(self):
		return self.age

pemain1 = Player2('ronaldo','69')
print('nama :',pemain1.get_nama(), 'age :',pemain1.get_age() )





## metode inheritence ( turunan )
print('\n# inheritence')

#parameter nya dari class Player2
class ArgentinaPlayer(Player2):

	def getNo(self, no):
		self.no = no
		return self.no

# tetap harus memasukan paramaeter dari parent class
argen = ArgentinaPlayer('ozil','32')
print(argen.get_nama(),'no',argen.getNo('7'))




## overide parent / pungsi yg sama dengan parent
print('\n# overide parent')
class Balap:
	def __init__(self, map, speed):
		self.map = map
		self.speed = speed

	def getMap(self):
		return self.map 

	def getSpeed(self):
		return self.speed

	def getCar(self):
		return 'Golf GT'

print('!parent class')
gass = Balap('city','140km/h')
print('map :',gass.getMap(),'speed :',gass.getSpeed(),'type car :',gass.getCar() )


# overide costume
class F1(Balap):
	def getCar(self):
		return 'ferarri'

# overide default
class Rally(Balap):
	 pass


race = F1('Sircuit','250km/h')
race2 = Rally('Jungle','100km/h')

print('\ncostum overide')
print('Map :',race.getMap(),'speed :',race.getSpeed(),'type car :',race.getCar())

print('\ndefault overide')
print('Map :',race2.getMap(),'speed :',race2.getSpeed(),'type car :',race2.getCar())




# mengakses class parent dengan metod super()
# fungsi nya untuk memanggil metode init/ lain nya dari parent class
print('\n# metode super()')
class Gp(Balap):
	def __init__(self, map, speed):
		super().__init__(map, speed)
		print('hello mark marques')

	def team(self):
		return 'redbull'

bike = Gp('mandalika','130km/h')
print(bike.getMap(), bike.team())

