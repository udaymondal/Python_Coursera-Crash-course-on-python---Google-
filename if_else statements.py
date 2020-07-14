def hint_username(username):
    if len(username) < 3:
        print("invalid")
    else:
        print("valid")

hint_username("us")




def is_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(6)


# logical functions

print(10>1)
print("cat" < "Cat")
print("candy" == "candy" or "dog" == "cat")



def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative





