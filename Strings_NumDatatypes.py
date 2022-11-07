print("Hello")  # string
print(2.3)  # float
print(12)  # integer

#calculation
print(10*4*4)
print(10+5*4)

print("20 days has how many mins")
print(20*24*60) #result is the value for 20 days having __ mins

#string concatenation
print(f"20 days has {20*24*60} mins") #latest syntax for string concat using f inside print() and this works for version starting from 3.6 and f stands for formatting

#variables
sum = 2+3
print(f"sum of 2 numbers is {sum}")

#Functions
calculation_mins = 24*60
units = "mins"


def days_cal(days,custom_message):   #defining function
    print(f"{days} days has {days * calculation_mins} {units}")
    print(custom_message)

#calling function
days_cal(35,"Good day") #passing values as parameters
days_cal(60,"Awesome!")

#return
def days_cal1(enter_value):   #defining function
    return f"{enter_value} days has {enter_value * calculation_mins} {units}" #returns the value

mins_cal = days_cal1(44) #stores return value
print(mins_cal) #prints return value

#user input
enter_value=int(input("User, Enter days value\n"))  #input takes string by default so it has to be converted to integer (int)

calculated_value = days_cal1(enter_value)
print(calculated_value)

#if else elif multiple conditional statements
def accept_pos_no(enter_value1):
    print(enter_value1 > 0) #prints True or False
    if enter_value1 > 0:
        return f"{enter_value1} days has {enter_value1 * calculation_mins} {units}"
    elif enter_value1 == 0:
        return "Value is equal to 0, result is 0"
    else:
        return "Invalid no"


enter_value1 = accept_pos_no(30)
print(enter_value1) #prints string " days has 28800 mins"
print(type(enter_value1)) #gives result as <class str>

# = -> assign & == -> equals

# try except

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.

#while loops
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  i = 0
  while i < 6:
      i += 1
      if i == 3:
          continue #stop when i=3 and starts next iteration & prints from 4 till cond fails
      print(i)


#List & for loops
#lists

fooditemslist = ["pizza","coke","garlic bread"]
for a in fooditemslist:
    print(a)








