
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

#Process 1

# user_input=input("Enter upto how many Fibonacci series to display ")
# sum=0
# for x in range(int(user_input)):
#
#     sum=sum+x
#     print(sum)
#
# print(f"The total  Fibonacci series is {sum}")

#Process 2

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



