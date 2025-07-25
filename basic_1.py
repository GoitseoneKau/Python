# print("Hello World")
# string type

# print(10)
# number type

# print(True)
# Boolean Type

# print(10.52)
# Float/Decimal type

# strings
# characterized by double quotes
test_string = "Hello Shudu"
string2 = "How are you?" 
part = string2[0:5]
# to get part of a string, use square brackets. i.e string[0:2], first part is the index i.e the 0, second is the length i.e the 2
# print(part)
# print(test_string + "," + string2)

# numbers and floats

# integers/whole numbers
# num1 = 10
# num2 = 15

# floats
# float_1 = 10.8
# float_2 = 4.323

# # result
# float_result = int(float_1) + float(num1)

# we can use integers for simple calculations, constants/quantities
# we can use floats for financial calculations, scientific calculations

# print/show result
# print(float_result)


# number operations

num1 = 10
num2 = 15
# addition
# result = num1 + num2

# # subtraction
# result = num1 - num2

# # division
# result = num1 / num2

# # multiplication
# result = num1 * num2

# modulus/remainder
result = 12 % 2



# boolean operations
# logic/bitwise operands

# and operation
# if both statements/operations are true, the result will be true
# if both statements are false, the result with be false
# if any one of the statements is false, the result is false
statement_1 = 10<2
statement_2 =  5<2 
result = statement_1 and statement_2

# or operation
# when either one of the statements are true, the result is true
# when both statements are true, the result is true
# when both statements are false, the result false

adult_age= 18
shudu_age = 15
goitse_age = 30

# check_goitse = goitse_age == young_teen_age
# check_shudu = shudu_age == young_teen_age
# are_both_of_young_adult_age = check_goitse or check_shudu

# are_either_one_of_them_adults = goitse_age>=adult_age or shudu_age>=adult_age

# married couple event example
no_of_people = 2
marriage_status = "married"

no_of_people_entering = 2

goitse_and_shudu_status = "married"

check_status = goitse_and_shudu_status == marriage_status
is_couple = no_of_people_entering == no_of_people
full_requirements = check_status and is_couple


# marriage orientation event example
married = True
unmarried = True
count = 2
people_who_came = 3

event_marriage_status_req = married or unmarried
event_people_count = people_who_came <= count

marriage_orientation_full_req = event_marriage_status_req and event_people_count

print(marriage_orientation_full_req)
