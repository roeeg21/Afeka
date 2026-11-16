
def q1():
    num = int(input("Enter a number: "))
    print(f"the remainder of {num} by 2 is {num%2}")

def q2():
    num = int(input("Enter a number: "))
    print(f"the unity digit of {num} is {num%10}")
    

def q3():
    num = int(input("Enter a number above 99: "))
    print(f"the right 2 digits of {num} is {str(num%100).rjust(2,"0")}")

def q4():
    num = int(input("Enter a number above 9: "))
    print(f"the {num} without the unity digit is {str(num//10).rjust(2,"0")}")


def q5():
    num = int(input("Enter a number above 99: "))
    print(f"the {num} without the 2 right digits is {str(num//100).rjust(2,"0")}")

def q6():
    num = int(input("Enter a number with 4 digits: "))
    time_format =f"{str(num//100%24).rjust(2,"0")}:{str(num%100%60).rjust(2,"0")}"
    print(f"{str(num)[0:2]} : {str(num)[1:3]} ")
    print(f"the time is {time_format}")

def q7():
    num = int(input("Enter a number with 4 digits: "))
    sum_of_2_right = num%10 + num%10//10
    sum_of_2_left = num//1000 + num//100%10
    print(f"does {num} meet the requirement? {sum_of_2_right == sum_of_2_left} ")

def q8():
    num = int(input("Enter a number with 2 digits: "))
    right_digit = num%10
    left_digit = num//10
    print(f"does {num} meet the requirement? {right_digit == 4 or left_digit == 4} ")

def q9():
    num = input("Enter a number with 4 digits: ")
    is_divided_by_3 = int(num) % 3 == 0
    is_polindrom = num[0] == num[-1] and num[1] == num[-2]
    print(f"does {num} meet the requirement? {is_divided_by_3 and is_polindrom} ")

def q10():
    num1 = int(input("Enter a number for quotient: "))
    num2 = int(input("Enter a number for divisor: "))
    print(f"{num1} / {num2} = {int((num1/num2)*100)/100 } ")

def q11():
    num = int(input("Enter a number: "))
    is_divided_by_2 = num % 2 == 0
    is_negative =  num < 0
    print(f"does {num} meet the requirement? {is_divided_by_2 or is_negative} ")


def q12():
    num = int(input("Enter a number with 2 digits: "))
    print(f"Is {num} not in range 10-20? {num >= 10 or num <=20}")


def main():
    q12()



if __name__ == '__main__':
    main()
    