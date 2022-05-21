"""print("Aryan")


#how the code excute in python
print('o----')
print(' ||||')
#in python the interpreter run the code line by line

print('*' * 10)#"""



#variable
"""
price=10
#print(price)
price=20
print(price)#here we will see that price value is been over written by price=20 because we know that python run the code line by line.
rating=4.9
name='mosh'
is_published=True#we use _(underscore) to seperate multiple word in our variable name
print(rating,name,is_published,price)


#excerise
full_name="john"
age=20
is_new=True
print(full_name,age,is_new)"""






#Getting input
"""name=input('what is your name?')#here we can see that input is a function which take input from use and save the input in variable name that can be further use

print("hi"+name)#output=what is your name?aryan
                     #hiaryan  """

#excercise 
"""name=input('what your name?')
color=input("fav color?")
print(name+' likes '+color)
"""


#Type Conversion
'''birth_year=input('Birth year:')
age=2019-birth_year
print(age)'''#this shit of code we give error for explanation plz refer your notes

'''birth_year=input('Birth year:')
age=2019-int(birth_year)#here new function int()has been launch to resolve above error
print(age)'''

'''birth_year=input('Birth year:')
print(type(birth_year))
age=2021-int(birth_year)#here new function int()has been launch to resolve above error
print(type(age))
print(age)
'''
#exercise
'''weight_lbs=input('weight (lbs):')
weight_kg=int(weight_lbs)*0.45
print(weight_kg)'''







#Strings
#course='python's coursefor beginners'#error
#course="python's course for beginners"
#course="python for "beginners""#error
course='python for "beginners"'
"""course='''hi john
love u for your support
my no=9188308042
thank u for receiving my email
'''
print(course)"""


#indexing in strings
'''
course='Python fro begineers'
#indexing 012345..........-2-1
print(course[0])#o/p=P
print(course[-2])#o/p=r
print(course[-1])#o/p=s
print(course[0:3])#o/p=Pyt
print(course[:5])#o/p=Pytho
print(course[:])#o/p=Python fro begineers
print(course[0:])#o/p=Python fro begineers
'''


'''
course='Python fro begineers'
another=course[:]
print(another)#o/p=Python fro begineers

'''

#exercise
name='jennifer'
print(name[1:-1])#o/p=ennife





