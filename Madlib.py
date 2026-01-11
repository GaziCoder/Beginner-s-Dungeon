# today we are gonna make a madlib......
#string concatenation aka how to put strings together.
from unicodedata import name


print('hello Gazi Baba!')
ab = 'Ariba Gazi'
print("The Topper of the University is " + ab)

#few ways to do this
print('The Topper of the University is {}'.format(ab))
print(f'The Topper of the University is {ab}')

name = input('Name: ')
h = input('Hobby: ')
o = input('Passion: ')
t = input ('Test: ')

madlib = (f"{name} is super-talented and Smart! {h} is her hobby. She is trying her best to excel \
in {h} She wants to become an {o} She is currently preparing for {t} Exam. Wish her luck!")

print(madlib)

#the code worked and i m so proud of myself.