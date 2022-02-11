# !/bin/python3
# Zeddnyx

'''
in python we have 4 type data ( integer as int, string as str, float and boolean/binary )

int = 5
str = 'hello world'
float = 5.4
bool = True/False
'''
print('Type data =======','\n=') # \n for new line
var1 = 5 # try to change to other type data 
print(var1)
#var1 is variable also u can change to other word but variable have rule, variable can't type first with number but can write with number!
# and 5 its value of variable and 5 its integer
# practice try to make it variable with int,str,float,bool

#for see the type data of variable we write using type like thia
print(type(var1))

#to make it easy when u run this code using string like this
print('this type data of ',type(var1))

'''
try to make simple variable  using type data bool,float,str and int
'''

print('\nCasting ============','\n=')
# casting its casting type data to another type data

#we gonna make it casting float to integer
var1 = 8
var2 = 8.3
print('before float casting to int')
print('var2 = ',var2)

var2 = int(var1)
print('after float casting to int')
print('var2 = ',var2)
print('')

# we gonna make it other type data to casting to other data
'''boolean just have to value (1-9 =  True and  0 = False )
'''
var1 = 9 # int
var2 = True
print('before boolean casting to int')
print(var2)

var2 = int(var1)
print('after casting boolean to int')
print(var2)
''' 
 try to casting another type data to make improvment
practice make it better'''


print('\nInput data','='*10)
# now we gonna try input data
#ex:
#input data can be casting to other type data
var1 = input('input any: ') # the value we input its gonna be string, try!
print('string', var1)

# input data casting to int
var2 = int(input('input numb: ')) # if u input a abcd or string u got  error
print('int', var2)

var3 = float(input('input numb: ')) # input numb the result its gonna be float. remember whats its float? if forget read the first instruction
print('float', var3)

var4 = bool(input('input numb: ')) # u still remember whats its boolean? its 0/1 0=False 1-9=True
# also when u input numb the result its gonna be True or False
print('float', var4)
'''using type data to see what type data u using'''
print('\ntype var4', type(var4))


# we gonna try operation math
# ( * - + / % // ** )
print('\noperation math', '='*10)
print(" + - /  * // % ") # fyi if using ( / floor divison ) the result is like float
var1 = 5
var2 = 3

var3 = var1 * var2 # in here im using *, u can change to other math, try to make it all of math 
print(var3)

# u can practice to make variable and with input data like this
# btw u should to casting 
var1 = int(input('numb '))
var2 = int(input('numb2 '))

result = var1 + var2 # im using + change to other operation
print('var1 + var2 =', result)
# remember to practice !!!

print('\nopartion precedence', '='*10)
''' order by precedence 
1. ()
2. **
3. math opration * / % //
4. plus + and min -
'''
a = 5
b = 3
c = 1

result = a ** b / c + a - c % a #kinda confused? don't worry u donna be understood
print(result)

# i change a little to make precedence
result2 = a + b / c + a  # THE RESULT ITS GONNS BE 13
print(result2)

result2 = a + b / (c + a) # im using precedence () so the result its gonna be
print(result2)

print('\noperation comparation', '='*10)
# > < >= <= == != is, is not
# the result its just True and False
a = 5
b = 3
result = a > b # > (bigger then) 
print('5 > 4 = ',result) # the reuslt its True cz 5 bigger then 4

#now <
result =  a < b # < (little then)
print('5 < 4 = ',result) # its gonna be False cz 5 little then 4 = False

# >=
result = a >= b
print('5 >= 4 = ',result)

# <=
result = a <= b
print('5 <= 4 = ',result)

# ==
result = a == b # its gonns be False cz 2 variable we write its not same value
print('5 == 4 = ',result)

# !=
result = a != b # its gonna be True cz 5 and 4 its not same
print('5 != 4 = ',result )

result = a  is b
print('5 is 4 = ',result)

# is not
result = a is not  b
print('5 is not 4 = ',result)


print('\nOperation not,or,and,xor(^)','='*10)
# the result its gonna be True and False
# not
a = True
b = not a
print(a,'not',b,' =',c)

#or
a = True
b = False
c = a or b
print(a,'or',b,'=',c) # if one value is True the result be True
# 1 or 1 = 1, 1 or 0 = 1, 0 or 1 = 1, 0 or 0 = 0

# and
c = a and b
print(a,'and',b,'=',c) # if 2 value is True the result be  True
'''1 and 1 = 1, 1 and 0 = 0, 0 and 1 = 0, 0 and 0 = 0'''

#xor ( ^ )
c = a ^ b
print(a,'^',b,'=',c) #be True if 1 of 2 value is True,  be False if 2 value True
#1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1, 0 ^ 0 = 0 


## distance number
print('\ncomparatin distance number ','='*10)

'''we use operation comparation, input data and casting
'''
var1 = int(input('input numb little then 3\nor bigger then 10 :'))
var2 = var1 < 3
print(var1,"little then 3",var2)

var2 = var1 > 10
print(var1,"bigger then 10",var2)

var1 = int(input("\ninput numb bigger then 3\nor little then 10 :"))

var2 = var1 > 3
print(var1,"bigger then 3",var2)

var2 = var1 < 10
print(var1,"little then 10",var2)

'''training distance numb'''
print("\ntrainig distance numb","="*10)
var1 = int(input("input numb little then 1\nbigger then 5\nbigger then 20\nlittle then 30 :"))

var2 = var1 < 1
print(var1,"liitle then 1",var2)

var3 = var1 > 5
print(var1,"bigger then 5",var3)

var4 = var1 > 20
print(var1,"bigger then 20",var4)

var5 = var1 < 30
print(var1,"little then 30",var5)

print("\noperation plus asigment","="*10)
print(" += -= *= /= %= ")
a = 5
print("before using plus asigment a = 5 :",a)

a += 2
print("after using plus asigment a += 2 :",a)

a /= 1
print("using divison  a /= 1 :",a)


print("\nMulti line/raw","="*10)
#this for using a multi line so u don't need print in every new line
print(r'''hollaa
world
also u can write whatever u want''') # the key is (r)


print("\nOpration and manipulation string","="*10)
first_name = "david"
middle_name = "alex"
print("before david and alex together")
print(first_name)
print(middle_name)

# using " " to makw spaces and u can use (,)(+)
name = first_name + " " + middle_name
print("\nafter david and alex together")
print(name)


print("\n\nCheck character","="*10)
a = "me"
b = "alex"
print(a)
print(b)
print("")

stats = a in name
find = b in name
print(a, "in name",name,(stats))
print(b,"in name",name,(find))


# format string
print('\n\nformat string','='*10)
a = 'zedd'
b = 'hallo'

c = f'{b},{a}'
print(c)
# the key of format string is ( f ) before using string


print("\n\npractice date and time",'='*10)

#the first we need to import library python
import datetime

day = datetime.date.today() # dont forget using()
print('date today is ',day)

# now we create a simple tools to count ur age
a = int(input('years u born :')) #this comand to ask your years of born
b = int(input('years now :')) # this comand to ask whats year rn
c = b - a   # and this gonna mines years rn to years ur born
print(c) # and boom ur gonna see age


print('\n\nif elif else','='*10)
# we gonna using input data,also if and friends, and format strin

a = input('who are u :') #this comand to ask 
if a == 'zedd':
	print('welcome',a)

elif a == "alex":    # if u using elif u can create lot of elif
	print('holla',a)

elif a == 'david':
	print('hallo',a)

else:   # else for statement wrong answer
	print("soory we don't know who u are")


print('\nloopping for,while','='*10)
numb = [1,4,6,8,9,5]
for x in numb:
	print(x) #the result its be value of numb

# practice
numb = range(1,7) # 1,7 not float but the reslut its gonna be list 1-8
for x in numb:
        print(x)

str1 = 'holla world'
for g in str1:
        print(g)


print('\nWhile looping','='*10)
'''looping no limit

numb = int(input('input numb bigger then 5 :'))
while numb > 5:
        print('this is result if u input numb bigger then 5')
'''

# practice
# we using input data,casting type data,operator comparation and while loop

numb = 0
loop = int(input('whats loop do u want :'))
while numb < loop :  # its gonna be looping when var(numb) little then var(loop)
        numb += 1    # and stop looping when var(numb) bigger then var(loop)
        print('gg')
print('end of while loop')


print('\nexception handling','='*10)
'''
x = 10

res = x / 0
print(res)

note: the result its error cz / can't floor by 0 the message 'ZeroDivisionError: division by zero'
'''
# but when u make tool and u want continue ur tool when get error
# the solution is using try and except

x = 10
try:
        res = x / 0
        print('passed')
except:
        print('error') # we change the mesage error like this
        print(x,"/ 0 = error, floor can't with 0")
# try to run the result its error and program not stop

try:
  x = int(input("input numb :"))
  assert x % 4 == 0

except:
  print ("[*] its not",x)

else:
  print ("[*] its",x)
  # the value of assert just  True and False



print('\n\nfunction','='*10)

# this very useful u must use def when write code cz make ur look like clean

def func1():
        print('hello world')

#when u want to call just like this
func1()


# can be like this
def numb():
        return 10 * 3

print(numb()) # the result is 30


# and function argument
def UrName(name):
        print('hello',name)

UrName('zedd')


# function argument math
def number(numb):
	return numb + 5

print(number(10))



print('\nManipulation list','='*10)

car = ['bmw','nissan','toyota','chevrollet','suzuki']
print(car)

#if u just wanna take 3 in 5 list is like this
car1 = car[0:3]
print(car1)

#okay right now we gonna update list car
car[1] = 'mercy'
print(car) # the output is nissan be change to mercy


# now we gonna remove list
del car[1]
print(car)

#count list car
print('length of list car is ',len(car))
