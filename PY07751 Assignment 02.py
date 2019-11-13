#Q1-------------------------------------------------------------------------------------
eng = int(input("Enter marks obtained in English subject : "))
maths = int(input("Enter marks obtained in Maths subject : "))
geo = int(input("Enter marks obtained in Geography subject : "))
sst = int(input("Enter marks obtained in Social Studies Subject : "))
sci = int(input("Enter marks obtained in Science subject : "))
#Calculating total marks
obtained = eng + maths + geo + sst + sci
total = (obtained/500) * 100
#Calculating grade
grade = "calculating"
if total < 50 :
    grade = "F"
elif total > 50 and total < 60 :
    grade = "D"
elif total > 60 and total < 70 :
    grade = "C"
elif total > 70 and total < 80 :
    grade = "B"
elif total > 80 and total < 90 :
    grade = "A"
else :
    grade = "A1"
print("Your grade is : " + grade)

#Q2-------------------------------------------------------------------------------------
num = int(input("Enter number : "))
if num % 2 == 0 :
    print(num, "is even.")
else :
    print(num, "is odd.")

#Q3-------------------------------------------------------------------------------------
my_list = ["Shaharyar", 131, 22, "A1", True]
print("Length of list is ", len(my_list))

#Q4-------------------------------------------------------------------------------------
list_sum = ["Hello", 72, 30]
total = 0
for x in list_sum :
    if isinstance(x, int) == True:
        total += x
print("sum of numeric items is : ", total)

#Q5-------------------------------------------------------------------------------------
numeric_list = [56, 32, 9, 45, 90, 33]
print(numeric_list)
print("Largest number in the list is", max(numeric_list))

#Q6-------------------------------------------------------------------------------------
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list_a, "\n")
print("List elements that are less than 5")
for i in list_a :
    if i < 5:
        print(i)