# ASSIGNMENT 09/25
#take the input for the start and stop value for a range.
# Then get the sum of odd and even numbers within that range using function or lambda and display that.


first_range=int(input("Enter the first range:"))
second_range = int(input("Enter the second range:"))
num= range(first_range,second_range)
even=list(filter(lambda x : x%2==0, num))
odd = list(filter(lambda x : x%2!=0, num))
even_sum=sum(even)
odd_sum=sum(odd)
print(even_sum)
print(odd_sum)













#Program to take user input of various data types and display string and integers separateky

# user_input=input("enter multiple integers separated by space:").split()
# new_list = [int(x) if x.isdigit() else x for x in user_input ]
# print(user_input)
# print(new_list)
# integer_list = [x for x in new_list if type(x) == int]
# string_list = [x for x in new_list if type(x) == str]
# print(integer_list)
# print(string_list)

#1. Fibonacci: a program that takes an input of how many terms to be displayed for the fibonacci sequence and
# then displays the total fibonacci sequence upto the number of terms specified


# user_input=input("Enter upto how many Fibonacci series to display ")
# int_userinput=int(user_input)
# def fibonacci(n):
#         if n <= 1:
#             return n
#         else:
#             return (fibonacci(n - 1) + fibonacci(n - 2))
#
#
# for x in range(int_userinput):
#     print(fibonacci(x))



# 2. Take input n and then displaye the factorial of that number

# user_input=input("Enter a number to find it's factorial ")
# intuser_input=int(user_input)
#
# def factorial():
#     factorial=1
#     if intuser_input < 0:
#         print("No factorial  for negative numbers!!!")
#     elif intuser_input == 0:
#         print("The factorial of 0 is 1.")
#     elif intuser_input>=0:
#         for i in range(1, intuser_input + 1):
#             factorial = factorial * i
#         print("The factorial of", intuser_input, "is", factorial)
#     else:
#         print("Try again!!")
# factorial()



