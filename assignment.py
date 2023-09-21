
#Program to take user input of various data types and display string and integers separateky

user_input=input("enter multiple integers separated by space:").split()
new_list = [int(x) if x.isdigit() else x for x in user_input ]
print(new_list)
integer_list = [x for x in new_list if type(x) == int]
string_list = [x for x in new_list if type(x) == str]
print(integer_list)
print(string_list)
