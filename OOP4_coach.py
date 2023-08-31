
class Student:
    name = 'Kapere'
    age = 12
    address = 'ntinda'
    phonenumber = 256753057575

    def assignment(): #method / behaviour
        num = 2+3
        # return 'Completes Assignment'
        #return num
        return [num,'completes assignment'] # this would return more than one item
    #fuction inside a class can be called a behavior of a class
#print(Student.assignment())
country = ['uganda','kenya','Rwanda','tanzania']
#items = Student.assignment # now the return is stored in the variable
for  item in country:
    print(item)
for item in range(4,10):
    print(item)


print('..............................')
cars = 1
while cars <= 10:
    #print(cars)
    cars +=2 # cars = cars + 1
    print(cars)

GPA = int(input('your grade: '))
if GPA < 0:
        print('Try fishing')
elif GPA == 1:
    print('do it')
elif GPA == 2:
    print('YOUR KAWA')
else:
    print('Good work')

