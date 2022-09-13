#display an info
print("display an info")
print("200 is a number")

# arithmetic opertion
print("arithmetic opertion")
print(20*24*60)

# string concatenation
print("string concatenation")
print("20 day are " + str(50) + " minutes" )

print(f"20 day are  {20*24*60*60} seconds")


# variable
print("variable")
calulateTotal= 24*60*60

print("calculate the total is " + str(calulateTotal))



#function
print("function")
def days_to_units(value,custom_message):
    print(f"{value} day are  {value*24*60*60} seconds")
    print(custom_message)

days_to_units(20,"awesome good!")

# get user input
user_input = input("what is value\n")
print(user_input)


# convert user input from string to int
print("convert user input from string to int")
main_input=input("enter input\n")
if main_input.isdigit():
     main_input_number=int(main_input)
     print(main_input_number)

#return value from a function

def area(length,width):
    return length* width


area = area(3,5)

print(area);




# conditionals expression
print("conditionals expression")
def age(age):
    if(age>0):
        print(age)
    elif(age==0):
        print("you entered 0")
    else:
        print("that an invalid age")

age(-4);








