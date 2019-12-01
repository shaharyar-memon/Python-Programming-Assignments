#Q1
my_dictionary = {
    'first_name' : 'Taufiq',
    'last_name' : 'Khan',
    'age' : 20,
    'city' : 'Karachi'
}

for each_key, each_value in my_dictionary.items():
    print(each_key, '\t:', each_value, '\n')

my_dictionary['Qualification'] = 'Intermediate' 
print(my_dictionary)

my_dictionary.update({'Qualification' : 'High Academic Level'})
print(my_dictionary)

del my_dictionary['Qualification']
print(my_dictionary)


#Q2
cities = {
    'Karachi' : {
        'country' : 'Pakistan',
        'population' : '14.91 million',
        'fact' : 'Business hub of Pakistan'
    },

    'Hyderabad' : {
        'country' : 'Pakistan',
        'population' : '1.733 million',
        'fact' : 'Sixth largest city of Pakistan in Sindh'
    },

    'Islamabad' : {
        'country' : 'Pakistan',
        'population' : '1.015 million',
        'fact' : 'Seat of Government of Pakistan'
    }
}

for each_city, city_info in cities.items():
    print(each_city, '\n', city_info, '\n\n')


#Q3
while True:
    age = int(input('User age? : '))

    if age == 0:
        print('Ending loop')
        break
    elif age < 3:
        print('Movie Ticket Price : FREE')
    elif age >= 3 and age <= 12:
        print('Movie Ticket Price : $10')
    elif age > 12:
        print('Movie Ticket Price : $15')


#Q4
def favorite_book(title):
    print('One of my favorite books is', title)

favorite_book('An Ember in the Ashes')


#Q5
import random

print('\n\n---Guess the number game---\n\n')
print('Generating hidden number...\n')
random_number = random.randrange(1, 30, 3)
#print(random_number)

def guess_the_num(random_number):
    i = 0
    while i < 3:
        num = int(input('Guess the number : '))
        if num < random_number:
            print('The entered number is smaller than the hidden number')
        elif num > random_number:
            print('The entered number is greater than the hidden number')
        else:
            print('Hoorah! You guessed the number! \nThe entered number is equal to the hidden number', random_number)
        i += 1

guess_the_num(random_number)
