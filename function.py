'''
Funtion
- tanpa parameter
- dengan argumen/paramter
- default parameter
- lebih dari sati parameter
- return parameter
'''

# tanpa parameter
def text():
	print('abc')

text()


# dengan argumen/parameter
def another_text(text2):
	print(text2)

another_text('abc2')


# parameter default
def default_text(text3 = 'Zero'):
	print(text3)

default_text()
# if u add new paramter, automatic will be change
default_text('new parm')



# lebih dari 1 parameter
def multi_parm(a,b):
	print('hasil',a,'+',b,'= ',a+b)

multi_parm(69,69)


# return parameter
def return_parm(a,b):
	return a+b

hasil = return_parm(10,10)
print(hasil)




'''
 *args dan **kwargs 
'''

"""   its gonna be error
def name(name1):
	print(name1)

name('ucok','udin')
"""

# *args
def name(*args):
	print(*args)

name('ucok','udin')
# boom the result not error



# **kwargs
def name2(**kwargs):
	for keyword,value in kwargs.items():
		print(keyword + "-"  + value)

name2(name = 'udin',hobby = 'study')
