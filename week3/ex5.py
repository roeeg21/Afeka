

def q1():
    temperature  = float(input("What is the temperature outside? "))
    cold_temperature = 11
    if temperature < cold_temperature:
        print("It's going to be a cold day")

def q2():
    user_age = int(input("What is your age? "))
    adult_age = 18
    if user_age > adult_age:
        print("You are adult")

def q3():
    temperature  = float(input("What is the temperature outside? "))
    cloudy = input("Is cloudy outside(yes/no) ? ")
    cold_temperature = 11 
    if temperature < cold_temperature and cloudy == "yes":
        print("It's going to rain")

def q4():
    jave_grade = int(input("Enter your grade in Java: "))
    python_grade = int(input("Enter your grade in Python: "))
    pass_grade = 60
    if jave_grade > pass_grade and python_grade > pass_grade:
        print("Registration for OOP course confirmed")

def q5():
    jave_grade = int(input("Enter your grade in Java: "))
    python_grade = int(input("Enter your grade in Python: "))
    pass_grade = 60
    if jave_grade > pass_grade or python_grade > pass_grade:
        print("Registration for OOP course confirmed")

def q6():
    temperature  = float(input("What is the temperature outside? "))
    cloudy = input("Is cloudy outside(yes/no) ? ")
    cold_temperature = 11 
    if temperature < cold_temperature and cloudy == "yes":
        print("It's going to rain")
    else:
        print("It's not going to rain")

def q7():
    num = input("Enter a 3-digit number: ")
    digit_3 = 3
    if int(num) % 2 == 0 and  digit_3 in num:
        print("The number meets the requirements.")
    else:
        print("The number does not meet the requirements because it is not even or does not contain the digit 3.")

def q8():
    side_a = int(input("Enter side a: "))
    side_b = int(input("Enter side b: "))
    side_c = int(input("Enter side c: "))
    if side_a + side_b > side_c:
        print("the numbers can be sides of triangel")
    elif side_b + side_c > side_a:
        print("the numbers can be sides of triangel")
    elif side_a + side_c > side_b:
        print("the numbers can be sides of triangel")
    else:
        print("the numbers cannot be sides of triangel")

def q9():
    num = int(input("Enter a number: "))
    if num > 9:
        print(f"{num} is 2-digits number")
    elif num > 99:
        print(f"{num} is 3-digits number")
    elif num > 999:
            print(f"{num} is 4-digits number")

def q10():
    grade = int(input("Enter a grade: "))
    excellent = 90
    very_good = 80
    passed = 60
    you_should_work_harder = 70
    if grade >= excellent:
        print("excellent")
    elif grade >= very_good:
        print("very_good")
    elif grade >= passed:
        print("passed")
    elif grade <= you_should_work_harder:
        print("passed\n you_should_work_harder")
    else:
        print("fail")


def q11():
    num1 = int(input("Enter a num1: "))
    operation = input("Enter a operation: ")
    num2 = int(input("Enter a num2: "))
    allow_operations = ["+","-","*"]
    if operation in allow_operations:
        if operation == "+":
            print(f"the result is {num1 + num2}")
        elif operation == "-":
            print(f"the result is {num1 - num2}")
        elif operation == "*":
            print(f"the result is {num1 * num2}")
    else:
        print("Invalid operation")



def q12():
    three_room_apartment = 120
    four_room_apartment = 150
    five_room_regular_apartment = 180
    five_room_duplex_apartment = 200
    rooms_in_apartment = input("Enter number of rooms in the apartment (3/4/5)")
    if rooms_in_apartment == "3":
        print(f"The amount to be paid is {three_room_apartment} NIS")
    elif rooms_in_apartment == "4":
        print(f"The amount to be paid is {four_room_apartment} NIS")
    elif rooms_in_apartment == "5":
        is_duplex = input("Is the apartment duplex(yes/no)? ")
        if is_duplex == "yes":
            print(f"The amount to be paid is {five_room_duplex_apartment} NIS")
        else:
            print(f"The amount to be paid is {five_room_regular_apartment} NIS")

def q13():
    num = int(input("Enter a num: "))
    result = "even" if num % 2 == 0 else "odd"
    print(f"{num} is {result} number")

def q14():
    num = int(input("Enter a num: "))
    result = "in" if num >= 10 and num <= 20 else "out of"
    print(f"{num} is {result} range")


def q15():
    num = int(input("Enter a num: "))
    result = "positive" if num > 0 else "negative" if num < 0 else "zero"
    print(f"{num} is {result} number")

def q16():
    year = int(input("Enter a year: "))
    result = "a leap" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "not a leap"
    print(f"{year} is {result} year")

def q17():
    list_31_days_in_month = 1,3,5,7,8,10,12,31
    list_30_days_in_month = 4,6,9,11,30
    feb_leap = 29
    feb_not_leap = 28
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))
    is_leap = True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
    days_in_month_check = (list_31_days_in_month[-1] if month in list_31_days_in_month else 
                           list_30_days_in_month[-1] if month in list_30_days_in_month else 
                           feb_leap if month == 2 and is_leap == True else feb_not_leap)
    print(f"Days in month {month} are {days_in_month_check} ")


def q18():
    num1 = int(input("Enter a num1: "))
    operation = input("Enter a operation: ")
    num2 = int(input("Enter a num2: "))
    allow_operations = "+","-","*","/"
    error_messege = "Invalid operation"
    error_messege_zero = "Can not divide by zero"
    check_value = (num1 + num2 if operation in allow_operations and operation == "+" else 
                   num1 - num2 if operation in allow_operations and operation == "-" else 
                   num1 * num2 if operation in allow_operations and operation == "*" else 
                   num1 / num2 if operation in allow_operations and operation == "/" and num2 != 0 else 
                   error_messege if operation not in allow_operations else error_messege_zero if num2 == 0 and operation == "/" else "")
    res = (f"the result is {check_value}" if check_value != error_messege and check_value != error_messege_zero else 
           error_messege if check_value == error_messege else error_messege_zero)
    print(res) 



def q19():
    height = int(input("What is the child's height? "))
    age = int(input("What is the child's age? "))
    calories = 700, 900, 1200
    valid = 40 <= height <= 140 and 0 <= age <= 8
    result = calories[0] if age <= 3 else calories[1] if height <= 100 else calories[2]
    print(f"The child should eat\n{result} per day" if valid else "Input out of range")


def q20():
    price = int(input("Enter price: "))
    items_amount = int(input("Enter number of items:  "))
    discount_over_3_items = 0.8 #20% discount 
    discount_over_300 = 50 #every 300 nis - 50 nis
    total_with_discount_over_300 = price - ((price - price%300)//300*discount_over_300)
    total_with_discount_over_3_items = price*discount_over_3_items if items_amount >= 3 else price
    total_price_to_pay = total_with_discount_over_300 if total_with_discount_over_300 < total_with_discount_over_3_items else total_with_discount_over_3_items 
    print(f"Your total payment is {total_price_to_pay} NIS")



def main():
    q20()

if __name__ == '__main__':
    main()
