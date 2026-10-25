###1. Write a Python program to print numbers from 1 to 10 using a while loop.
i = 1
while(i<=10):
    print(i)
    i = i+1


###2. Write a program to print numbers from 10 down to 1 using a while loop.(Hint: start from 10 and decrease the counter each time.)
i =10 
while ( i >= 1):
    print(i)
    i = i-1

###3. Write a program to print all even numbers between 1 and 50 using a whileloop.(Hint: Use the modulus operator % to check for even numbers.)Example Output: 2 4 6 8 ... 50
num = 1
while num<= 50:
    if (num % 2 == 0):
        print(num)
    num = num +1

###4. Write a program that prints the sum of first n natural numbers.
#For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.
#(Hint: Keep a running total inside the loop.)

n = 5
sum = 0
while( n >= 1):
    sum = sum + n
    print(sum)
    n = n - 1


#5. Write a program to print this pattern using a while loop:
#  *
#  * *
#  * * *
#  * * * *

i=1
while i<=4:
    print("*"*i)
    i = i+1

##6. Saumya wants to print her name 5 times, but each time with a number in
#front of it. Write a program using a while loop that prints:
#1. Saumya Singh
#2. Saumya Singh
#3. Saumya Singh
#4. Saumya Singh
#5. Saumya Singh

name =  "Saumya Singh"
for i in range (1,6):
    print(f"{i}.{name}")

###7. Write a program to print the multiplication table of any number using a while
#loop.
i =1 
n =10
while(i <=10):
    print(f"{n} * {i} = {n*i}")
    i = i+1

##8. Write a program using for and range() to print all even numbers between 1
#and 20.

for i in range(2,21,2):
    print(i)

##9. Write a program to print numbers from 1 to 50, but print "Saumya Singh"
#instead of numbers that are multiples of 5.
#Example Output: 1 2 3 4 Saumya Singh 6 7 8 9 Saumya Singh ...

for num in range(1,51):
    if num % 5 == 0:
        print("saumya singh", end = " ")
    else:
        print(num, end = " ")



#10.Write a program to print the square of each number from 1 to 10 using a for
#oop.
i = 1
for i in range(1,11):
    print(f"{i**2}")
    i = i+1


#11.Write a program that prints the multiplication table of any number entered by
#the user using a for loop.
i = 1
num = int(input("enter a number:"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
    i =i+1

#12.Write a program that prints all numbers from 100 to 1 using for and range().

for i in range(100,1,-1):
    print(i)
    i = i+1

##13.Saumya wants to print her username five times in uppercase letters.
name = "ashu"
name_upper = name.upper()
print((name_upper  +"\n")*5)

#using for loop
name = "ashu"
upperName = name.upper()
for i in range (1,6):
    print(upperName)
    i = i+1


##14.You are given a list of Saumya’s favorite foods. Write a Python program to
#print each food item using a for loop.
foods = ["dosa","idli","chapati"]
for i in range(1):
    print(foods)


##15.Saumya has created a tuple of countries she has already traveled to. Write a
#s_traveled = ("Malaysia", "Vietnam", "Switzerland", "Italy", "Bhutan")

countries_traveled = ("Malaysia", "Vietnam", "Switzerland", "Italy", "Bhutan")
for el in range(1):
    print(countries_traveled)


##1. Print numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)

#2. Print numbers from 100 to 1 using a while loop.
i =100
while i>= 1:
    print(i)
    i = i-1

#3. Print all numbers between 1 and 50 except multiples of 5.
for i in range(1,51):
    if (i % 5 != 0):
        print(i)
    i = i+1


#4. Create a program that asks the user for 5 favorite foods and prints them one
#by one.
food1 = input("enter 1st food:")
food2 = input("enter 2nd food:")
food3 = input("enter 3rd food:")
food4 = input("enter 4th food:")
food5 = input("enter 5th food:")
print(food1)
print(food2)
print(food3)
print(food4)
print(food5)

#5. Print the sum of first 10 natural numbers using a while loop.
i =1
sum = 0
while i <= 10:
    sum = sum + i
    print(sum)
    i = i+1