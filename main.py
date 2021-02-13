#Credits:
#This file was coded by _NooberrUwU#7048.
#This file is an open-source code, everyone can take this code for thier own!
#Any bug or error occurs in runtime, please let me know. I'll fix them ASAP!

#The function checks the input number is valid or not.
#If true, returns a floated-number value. Else (False), returns an empty string.
def check_input(number):
  try:
    float(number)
    return float(number)
  except:
    return ""

#Main loop
while True:
  #Input the values.
  a = input("Input \"a\": ")
  b = input("Input \"b\": ")

  #Execute the value check function.
  a = check_input(a)
  b = check_input(b)

  #If statement: If both "a" value and "b" value are valid, execute the main calculate function. Else, the file will print the error sentence.
  if a and b:
    str_a = str(a)
    str_b = str(b)
  
    #If "a" value or "b" value is 1, they will disappear in the equation. (They won't stay 1 in original equation but still be used in equation solving progress)
    if a == 1:
      str_a = ""
    if b == 1:
      str_b = ""

    #The original equation
    e = "{a}x + {b} = 0".format(a = str_a, b = str_b)

    #Print the original equation
    print("The equation is: " + e)

    #In case "a" value and "b" value are 0, the equation will have infinity solutions.
    if a == 0 and b == 0:
      print("\t<=> 0x = 0")
      print("\t => The equation has infinite number of solutions!")
      print("\n")

    #In case "a" value equals 0 but "b" is not 0, the equation won't have any solution.
    elif a == 0 and b != 0:
      print("\t<=> 0x = -{b}".format(b = str(b)))
      print("\t => The equation doesn't have any solution!")
      print("\n")

    #Else (normal equations), solve it normally.
    else:
      solution = -b / a
      print("\t<=> {a}x = -{b}".format(a = str(a), b = str(b)))
      print("\t<=> x = -{b} / {a}".format(a = str(a), b = str(b)))
      print("\t<=> x = " + str(solution))
      print("The solution of the equation is " + str(solution))
      print("\n")

  #The error message.
  else:
    print("At least one value which you have input was invalid!")
    print("\n")