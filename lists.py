'''
name=['john','bob','dsa','asd','sfas']
#print(name[0])
#print(name[-1])
#print(name[2])
#print(name[2:4])
#print(name[2:])
#print(name[0:])
name[0]='jon'
print(name)

'''





#Exercise
#Write a program to find the largest no. in a list
numbers=[3,6,2,8,4,10]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)        