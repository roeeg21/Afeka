from math import gcd

def q1():
    res = ""
    num = int(input("Enter num between 0 to 20: "))
    index = 1
    if (num >=0 and num<=20):
        while(index <= num):
            res += f"{index}\t"
            index += 1
    else:
        res = "invalid input"
    print(res)


def q2():
    res = ""
    num = int(input("Enter num between 0 to 20: "))
    if (num >=0 and num<=20):
        while(num > 0):
            res += f"{num}\t"
            num -= 1
    else:
        res = "invalid input"
    print(res)

def q3():
    sum_of_digit = 0
    num = int(input("Enter num between 0 to 100: "))
    index = 1
    if (num >=0 and num<=100):
        while (index <= num):
            sum_of_digit += index
            index += 1
    else:
        res = "invalid input"
    print(f"sum numbers from 1 to {num} is {sum_of_digit}")

def q4():
    sum_of_even_digit = 0
    num = int(input("Enter num between 0 to 100: "))
    index = 0
    if (num >=0 and num<=100):
        while (index <= num):
            sum_of_even_digit += index
            index += 2
    else:
        res = "invalid input"
    print(f"sum of even numbers from 1 to {num} is {sum_of_even_digit}")

def q5():
    sum_of_digit = 0 
    num = int(input("Enter num between 0 to 100: "))
    while (num != 0):
        sum_of_digit += num
        num = int(input("Enter num between 0 to 100: "))
    print(f"sum numbers is {sum_of_digit}")


def q6():
    num_of_digit = 0 
    num = int(input("Enter num: "))
    temp_num = num
    while (num != 0):
        num_of_digit += 1
        num = num // 10
    print(f"the number {temp_num} has {num_of_digit} digits")

def q7():
    sum_of_digits = 0
    num = int(input("Enter num: "))
    temp_num = num
    while (temp_num != 0):
        sum_of_digits += temp_num % 10
        temp_num = temp_num // 10
    print(f"sum of digits of {num} is {sum_of_digits}")

def q8():
    sum_of_digits = 0
    num = int(input("Enter num: "))
    temp_num = num
    while (temp_num != 0):
        if ((temp_num%10) % 2 == 0):
            sum_of_digits += temp_num % 10
            temp_num = temp_num // 10
        else:
            temp_num = temp_num // 10
    print(f"sum of even digits of {num} is {sum_of_digits}")

def q9():
    num = int(input("Enter num: "))
    res = ""
    index_rows = 1
    index_colums = 1
    if num <= 10 :
        while index_rows <= num:
            while index_colums <= num:
                res += "* "
                index_colums += 1
            res += "\n"
            index_colums = 1
            index_rows += 1
    print(res)



def q10():
    num = int(input("Enter num: "))
    res = ""
    space = " "
    index_rows = 1
    num_of_symble = 1
    if num <= 10 :
        while index_rows <= num:
            while num_of_symble <= num:
                res += (num-num_of_symble)*space
                res += "* "*num_of_symble
                num_of_symble += 1
                res += "\n"
            index_rows += 1
    print(res)

def q11():
    sring = input("Enter a string: ")
    index = 0
    res = ""
    while (index < len(sring)):
        if sring[index] >= 'A' and  sring[index]<= 'Z':
           res += sring[index]
        elif res == "":
            res = "No capital letters"
        index += 1
    print(res)

def q12():
    string = input("Enter a string: ")
    char = input("Enter a char: ")
    sum_of_char = 0
    index = 0
    while (index < len(string)):
        if string[index] == char:
            sum_of_char += 1
        
        index += 1
    print(sum_of_char) 

def q13():
    string = input("Enter a string: ")
    space = " "
    res = ""
    index = 0
    while (index < len(string) and string[index] != '!'):
        if string[index] != space:
            res += string[index]
        index += 1
    print(res)

def q14():
    string = input("Enter a string: ")
    char = input("Enter a char: ")
    res = f"Charcter {char} found in index "
    index = 0
    while (index < len(string)):
        if string[index] == char:
            res += str(index)
            index = len(string)
        else:
            index += 1
    print(res)


def q15():
    num = int(input("Enter num: "))
    temp = num
    binary = ""
    if num == 0:
        binary = "0"
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //=  2
    print(f"{num} is {binary} -> with func bin {bin(num)}")

def q16():
    num = int(input("Enter num: "))
    temp = num
    hexa = ""
    digits = "0123456789ABCDEF"
    if num == 0:
        hexa = "0"
    while temp > 0:
        hexa = digits[temp % 16] + hexa
        temp //=  16
    print(f"{num} is {hexa} -> with func hex {hex(num)}")

def q17():
    num = int(input("Enter num: "))
    divisor = 2
    is_prime = num > 1
    while divisor < num and is_prime:
        if num % divisor == 0:
           is_prime = False
        divisor += 1
    print(f"{num} is a prime number? {is_prime}")

def q18():
    num1 = int(input("Enter num: "))
    num2 = int(input("Enter num: "))
    index = 1
    res = 0
    while index <= num2:
        res += num1
        index += 1  
    print(f"Multiply = {res}")

def q19():
    num = int(input("Enter num: "))
    divisor = 2
    temp = num
    res = "1"
    while temp > 1:
        if temp % divisor == 0:
           res += f" X {divisor}"
           temp //= divisor
        else:
            divisor += 1
    print(f"{num} = {res}")

def q20():
    num1 = int(input("Enter num: "))
    num2 = int(input("Enter num: "))
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    print(f"biggest common divide: {num1} -> with func gcd {gcd(num1,num2)}")


def main(): 
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    #q7()
    #q8()
    #q9()
    #q10()
    #q11()
    #q12()
    #q13()
    #q14()
    #q15()
    #q16()
    #q17()
    #q18()
    #q19()
    q20()


if __name__ == '__main__':
    main()
