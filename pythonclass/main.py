# class Student:
#     def __init__(self, sid, name,rank, address):
#
#             self.sid = sid
#             self.name = name
#             self.rank=rank
#             self.address=address
#     def details(self):
#            print(f'id={self.sid}\nname={self.name}\nrank = {self.rank}\naddress = {self.address}')
#
#
# s=Student(1,"Garisha","5","Kalanki")
#
# s.details()
#
#

# a= "My name is Garisha Neupane"
# print(a[1:10:2])

# b= 'Garisha '
# y=a+b
# x=b*4
# print(x)
# print(y)
# print(len(y))
#
# b='this is python cLass'
# up=b.upper()
# lw=b.lower()
# cp=b.capitalize()
# tl=b.title()
# print(up)
# print(lw)
# print(cp)
# print(tl)

# animals="cat,dog,rabbit,horse"
# spliting=animals.split(",")
# print(spliting)

# animals=['cat','dog','rabbit','horse']  #list
# delimiter=";"
# joining=delimiter.join(animals)
# print(joining)

# b = 'this is python cLass'
# locate=

#ListDataType
# test_list=[1,'Garisha', 'Damauli']
# print(test_list)
# empty_list=[]
# empty_list.append("Neupane")
# empty_list.append("Garisha")#method changes original value
# print(empty_list)
# empty_list.remove(empty_list[1])
# print(empty_list)

# test_list=[10,50,12,55,85,67]
# adding=[4,5]
# test_list.append(adding)
# test_listt=test_list+adding
# print(test_listt)
# print(test_listt[6])
# # print(test_list.sort()) ##notworking
# t=len(test_list) #function doesn't change original value
# m=max(test_list)
# print(t)
# print(m)

#TupleDataType

# tupleeg=(1,2,3,4,5,6)
# print(tupleeg[3]) #cannot be changed once created

#tuplepacking
# raw='ram',1,65,45

#tupleunpacking
# a,b,c,d=raw
# print(c)

#dictDataTypes #key value pair

# person={"id":1 ,"name":'Garisha', "Address":'Tanahun'}
# print(person["Address"])
# student={('ram','math'):67 , ('hari','math'):97}
# score=student[('hari','math')]
# print("Hari's math score is:", score)

#set
# a={1,2,3}
# b={4,5,6}
# unione= a|b
# print(unione)
# a.add(10)
# print(a)
# multipleadd={100,20,30}
# a.update(multipleadd)
# print(a)

#TypeCasting
# x=58.55
# y=int(x)
# print(y)
# student=['Garisha',1,'Damauli',11]
# student_tuple=tuple(student)
# student_list=list(student_tuple)
# print(student_tuple)
# print(student_list)
# print(student)

# h


#input_output_cmd

# user_imput=input("Hello, What is your name?")
# print("The value entered is ", user_imput)

#Check if at least one argument is provided(the script name itself)
# import sys
# if len(sys.argv)<2:
#     print("Usage")
# else:
#     user_input=sys.argv[1]
#     print("You Entered:", user_input)




#IFELS



# user_input = input('user string ?')
# reversed_string = user_input[::-1]  #logic to reverse then string
#
# if(user_input == reversed_string):
#     print('The string is Palindrome')
# else:
#     print('Not palindrome')

# for i in range(0,10,3):
#     print(i)
#
# number_list=list(range(0,20,5))
# print(number_list)

#whileLoop

# count=0
# while(count<5):
#     print(count)
#     count+=1


# for i in range(1,5):
#     if(i==3):
#         continue;
#     else:
#         print(i)

# for i in range(1,5):
#     if(i==3):
#         break;
#     else:
#         print(i)

# list_example=['a','b','c','d']
# for i in list_example:
#     if(i=='c'):
#         continue
#      print(i)


#forelse
# for num in range(5):
#     if num==6:
#         print("number is found")
#         break
# else:
#     print("Not found")
#

# Program to check if a number is prime or not
#
# num = int(input("Enter a number: "))
#
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

#remove odds

# number = [2,4,5,9,18,20]
# empty_list=[]
# for i in number:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)



#rasila
# num_list = [2,4,5,6,3,9]
# even=[]
# for i in num_list:
#     if i%2!=0:
#         continue
#     else:
#         even.append(i)
# print(even)

#sonal
# num = [2,4,5,9,18,20]
# new=[]
# count = 0
# for i in num:
#     if (i % 2) == 0:
#         # new.append(i)
#         new.insert(count, i) #insert(x,y) y is appended in x position
# print(new)

#List Comphrension
# number_list = [2, 4, 5, 9, 18, 20]
# filtered_list = [x for x in number_list if x % 2 == 0]
# print(filtered_list)




# num_list=list(range(1,10))
# print(num_list)
# square=[x**2 for x in num_list]
# print(square)

# fruits=["apple","kiwi","mango"]
# uppercase= [x.upper() for x in fruits]
# print(fruits)

# num=[1,2.3,4,5.5,6,7]
# integer=[x for x in num if type(x)==int]  #integers_only = [x for x in num if isinstance(x, int)]
# print(integer)

# num1=input("enter first number")
# num2=input("enter second number")
# num3=input("enter third number")
# number=[num1,num2,num3]
# maximum=[max(x) for x in number]
# print(maximum)

# user_input=input("enter multiple integers separated by space:")
# split_input = user_input.split() # to take multiple inputs
# inputs=[float(x) for x in split_input]
# max_value=max(inputs)
# print(max_value)

# user_input=input("enter multiple integers separated by space:").split()
# new_list = [int(x) if x.isdigit() else x for x in user_input ]
# print(new_list)
# integer_list = [x for x in new_list if type(x) == int]
# string_list = [x for x in new_list if type(x) == str]
# print(integer_list)
# print(string_list)

#PYTHON_FUNCTIONS

# def python_test(a,b):
#     # docstring
#     """
#
#     :param a:
#     :param b:
#     :return:
#
#     """
#
#
#     print(a)
#     print(b)
#     sum=a+b
#     return sum
#
#
# output=python_test(5,10)
# print(output)

# def o_fun():
#     o_var=54
#
#     def i_fun():
#         nonlocal o_var
#         o_var=5
#     i_fun()
#


# def cube(num):
#     return num**3
#
# num=input("enter a number:")
#
#
# cubenum=cube(int(num))
# print(f"The cube of { num } is { cubenum}")

##Recursive Function
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n *factorial(n-1)
# val = int(input("Enter a positive number"))
#
# print(f"Factorial of {val} is {factorial(val)}")

# def check(n):
#     if n<0:
#         return
#     else:
#         print(n)
#         check(n-1)
# check(6)


#lambda arguments : expression

# add= lambda a,b: a+b
# print(add(3,4))

#filter function

# num=[1,2,3,4,5,6]
# even=list(filter(lambda x : x%2==0, num))
# print(even)

#map function

# num=[1,2,3,4,5,6]
# square=list(map(lambda x: x**2, num))
# print(square)

#multiple operations in lambda

# operation = [lambda x,y:x+y, lambda x,y:x-y]
#
# val1=operation[0](3,4)
# val2=operation[1](4,3)
# print(val1,val2)

#Shadowing

# x=1
#
# def func():
#     global x ##changes the global value remaining inside funcion
#     x=8
#     y=5
#     print(x)
#     def fun1():
#         nonlocal y
#         y=10
#         print(y)

#Shadowing(needs to be prevented)
# x=1
# def fun(x):
#     print(x)
# fun(5)



#File Handling
#Reading contents from employee.txt file

# emp_file=open("employee.txt", 'r')
# print(emp_file.readable()) #returns true
# print(emp_file.read(3))
# print(emp_file.read(3)) #Continues reading from previous index
# print(emp_file.readline())
# print(emp_file.readlines()) #returns each line in list
#
# for emp in emp_file.readlines(): ## Not to return each lines in list.
#     print(emp)
# emp_file.close()

#a-apends without overriding (a+ also reads)
# w-writes with overriding (w+ also reads)
# emp_file=open("employee.txt","a")
# emp_file.write("\nThis is write command") #overides whatever is in file
# emp_file.close()

#context manager

# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file= open(self.filename,self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with FileManager("test.txt", "w") as f:
#     f.write("Hi")
#
#
# print(f.closed)


#EXCEPTION HANDLING

# try,except,finally
#raise - to raise exception by yourself

# Create a file ‘student.txt’ that contains students’ name, gender, and grade. Write a program to read individual lines
# and copy each line of the file and write in another file using for loop. The content should be in uppercase.
# Use context manager.

# class studentfile():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file= open(self.filename,self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
# with studentfile('student.txt', 'r') as a, studentfile('studentnew.txt', 'w') as b:
#         for text in a:
#             content=text.upper()
#             b.write(content)
# print("Copied")
# print(a.close())
#
# OR only this

# with open('student.txt', 'r') as a, open('studentnew.txt', 'w') as b:
#     for text in a:
#         content = text.upper()
#         b.write(content)
# print("Copied")
# print(a.close())



#INHERITANCE

class Person:
    def __init__(self,name,id):
        self.name = name
        self.id =id
    def display(self):
        print(self.name,self.id)

class Emp(Person):

    def __init__(self,name,id,department):
        Person.__init__(self,name,id)
        self.dept = department
    def employee(self):
        # print(self.dept)
        print(f"my name is {self.name} with id {self.id} in department {self.dept}")

E = Emp("Mario",103,"computer")
E.employee()










