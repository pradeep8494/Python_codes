#Strings -
print("This is first line \nThis is second line") #Note - After back slash if any space that will be taken in new line
print("This is before space \t it's after space")
print("quotes inside quote is \"pradeepa\" ")

#typecasting - implicit and explicit
a, b = 10, 2.0
c = a + b
print(f"After implicit typecast {c}")

Int = 10
afterTypeCast = float(Int)
print(f"After explicit typecast {afterTypeCast}")

strOne = "String1"
strTwo = "String2"
print(f"String concatination using + opr  {strOne + '' + strTwo}")  # Here we can add Manuall space
print(f"String concatination using ',' opr {strOne,strTwo}") #Here we space will explcitly(Programaticlly we can add not manually)
print(f"String concatination using using format string spcifier  {strOne} {strTwo}")
print(strOne,strTwo)

lst = ["value1", 1, "value2", 2] #collection of diffrent Data
lst[0] = "val2" #mutable
print(f"after mutable opr {lst}")

#Convert string to List -  split
strValue = "This is string and converting to list"
i_am_list = strValue.split()
print(f"After converting string to list {i_am_list}")

#Convert List to string - join
i_am_string = ""
lstValue = ["i", "am", "list"]
i_am_string.join(lstValue)
print(f"After Converting from list to string {i_am_string}")
