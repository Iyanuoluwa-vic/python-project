#display an info
print("200 is a number")

# arithmetic opertion
print(20*24*60)

# string concatenation
print("20 day are " + str(50) + " minutes" )

print(f"20 day are  {20*24*60*60} seconds")


# variable
calulateTotal= 24*60*60

print("calculate the total is " + str(calulateTotal))



#function
def days_to_units(value,custom_message):
    print(f"{value} day are  {value*24*60*60} seconds")
    print(custom_message)

days_to_units(20,"awesome good!")

# get user input
user_input = input("what is value\n")
print(user_input)


# convert user input from string to int
main_input=input("enter input")
main_input_number=int(main_input)
print(main_input_number)

#return value from a function

def area(length,width):
    return length* width


area = area(3,5)

print(area);













