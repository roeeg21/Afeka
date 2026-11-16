

# Exercise 1: Print all numbers from 1 to 10.
def q1():
    res = ""
    for index in range(1,11):
        res += str(index)+" "
    print(res)



# Exercise 2: Print all even numbers from 2 to 20.
def q2():
    res = ""
    for index in range(2,21,2):
        res += str(index)+" "
    print(res)


# Exercise 3: Print all odd numbers from 1 to 19.
def q3():
    res = ""
    for index in range(1,20,2):
        res += str(index)+" "
    print(res)


# Exercise 4: Ask the user for a number N and print all numbers from 1 to N.
def q4():
    num = int(input("Enter num: "))
    res = ""
    for index in range(1,num+1):
        res += str(index)+" "
    print(res)


# Exercise 5: Print all numbers from 10 down to 1.
def q5():
    res = ""
    for index in range(10,0,-1):
        res += str(index)+" "
    print(res)


# Exercise 6: Calculate and print the sum of all numbers from 1 to 100.
def q6():
    res_sum = 0
    for index in range(1,101):
        res_sum += index
    print(res_sum)


# Exercise 7: Ask the user for a number and print its multiplication table from 1 to 10.
def q7():
    num = int(input("Enter num: "))
    res = ""
    for index in range(1,11):
        res += f"{num} X {index} = {num * index}\n"
    print(res)



def q8():
    pass



def q9():
    pass



def q10():
    pass

def q11():
    pass

def q12():
    pass

def q13():
    pass

def q14():
    pass

def q15():
    pass

def q16():
    pass

def q17():
    pass

def q18():
    pass

def q19():
    pass

def q20():
    pass

def main():
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    q7()
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
    #q20()

if __name__ == '__main__':
    main()
