def area_triangle(base, height):
    return ((base*height)/2)

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b
diff = area_b - area_a

print("The sum of both areas is " + str(sum) + " and difference is " + str(diff))


# parameterpasser 2nd

def month_days (month, days):
    print(month + " has " + str(days) + " days")

month_days("june","30")
month_days("july", "31")

month_days("February", "28")
#namwe = "udaysankarmondal"
#print(len(namwe))


#lucky LEN number
def lucky_number(name):
    number  = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))


lucky_number("Kay")
lucky_number("Cameron")


