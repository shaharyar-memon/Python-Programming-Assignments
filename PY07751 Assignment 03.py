#Q1
num1 = int(input('Enter first value : '))
num2 = int(input('Enter second value : '))
op = input('Enter operation : ')
ans = 0 

if op == '+':
    ans = num1 + num2
elif op == '-':
    ans = num1 - num2
elif op == '*':
    ans = num1 * num2
elif op == '/':
    ans = num1 / num2
elif op == '**':
    ans = num1**num2
else:
    print('Invalid operator') 

print(ans)

#Q2
my_list = [2, 3, 'chewing gum', 'False']
count = 0

for i in my_list:
    if isinstance(i, int) == True:
        count += 1
print('There are', count, "numeric values in the list ", my_list)


#Q3
student = {
    'name': 'Shaharyar',
    'roll_no' : 'PY07751'
}

print(student)
student['interest'] = 'Python'
print(student)
student.update({'interest': 'Machine Learning', 'new key': 'This is a new key'})
print(student)

#Q4 
random = {
    'name': 'Shaharyar',
    'roll_no': 'PY07751',
    'num1': 12,
    'interest': 'Machine Learning',
    'num2': 10
}

sum = 0 

for each_value in random.values():
    if isinstance(each_value, int) == True:
        sum += each_value

print(sum)

#Q5 
list_01 = ['list', 'saylani', 3, 5, 'saylani', True, False, True]
print(list_01)
list_dup = []

for i in list_01:
    if list_01.count(i) > 1:
        list_dup.append(i)

for j in list_dup:
    if list_dup.count(i) > 1:
        del list_dup[i]

print('Elements that have duplicates :', list_dup)

#Q6 
my_dictionary = {
    0: 1,
    1: 2,
    2: 3
}

check = int(input('Enter key to check if it already exists : '))
if check in my_dictionary.keys():
    print(check, 'already exists in the dictionary.')
else:
    print(check, 'does not exist in the dictionary.')