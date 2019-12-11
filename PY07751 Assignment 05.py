#Q1
def factorial(n):
    fact = 1
    if n == 0:
        return fact
    else:
        fact = n * factorial(n-1)
        return fact
n=int(input("Enter number: "))
print(factorial(n))

#Q2
def my_string_func(sentence):
    u_case = 0
    l_case = 0
    for i in sentence:
        if i.isupper():
           u_case+=1
        else:
           l_case+=1
    print ("no.of uppercase letters: ", u_case)
    print ("no.of lowercase letters: ", l_case)

my_string_func("Dil Dil Pakistan")

#Q3 
def even_numbers(listylist):
    even_list = []
    for i in listylist:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)
        
mylist = [2, 4, 5, 6, 8, 1]
even_numbers(mylist)

#Q4
def palindrome_check(sentence):
	l_pos = 0
	r_pos = len(sentence) - 1
	
	while r_pos >= l_pos:
		if sentence[l_pos] != sentence[r_pos]:
			return False
		l_pos += 1
		r_pos -= 1
	return True

print(palindrome_check('madam'))

#Q5
def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True    

print(is_prime(2))

#Q6
def shopping_cart(*items):
    for item in items:
        print(item)

shopping_cart("Bread", "Eggs", "Vegetables", "Fruit")