import math
# def example():
    # num = input("Enter num : ")
    # print(num)

def q1(): #gets name and prints the name
    name = input("What is your name: ")
    print(f"Your name is: {name}")
        

def q2(): #gets age and prints the age in five years
    age = input("What is your age: ")
    print(f"Your age is: {age}, in five years your age will be {int(age)+5}")

def q3():# gets radius of a circle and prints the primeter and area of the circle
    radius = float(input("What the radius of the circle: "))
    pi = 3.14
    print(f"radius = {radius}, primeter = {round(2*pi*radius,2)}, area = {round(pi*radius**2,2)}")
    """
        primeter = 2*math.pi*radius
        area = math.pi*math.pow(radius,2)
        print(f"radius = {radius}, primeter = {round(primeter,2)}, area = {round(area,2)}")
    """

def q4(): # gets length and width of a rectangle and prints the primeter and area of the rectangle
    length = float(input("Enter the legnth of the ractangle: "))
    width = float(input("Enter the width of the ractangle: "))
    print(f"length = {length}, width = {width}, primeter = {2*length + (2*width)}, area = {length*width}")

def q5(): # gets 3 chars and prints them in 3 lines
    chars = input("Enter 3 chars: ")
    print(f"{chars[0]}\n{chars[1]}\n{chars[2]}")

def q6():# gets 3 chars and prints them in one line with tab between them
    chars = input("Enter 3 chars: ")
    print(f"{chars[0]}\t{chars[1]}\t{chars[2]}")

def q7():# gets one char and prints the ASCII value of the char
    char = input("Enter one char: ")
    print(f"{char} is represent {ord(char)} charcter")


def q8():# gets one ASCII value and prints the char represented by the ASCII value
    num = int(input("Enter ASCII value: "))
    print(f"{num} is represent {chr(num)} charcter")

def q9():# gets one capital letter and prints the lower letter represented by the capital letter
    char = input("Enter one cappital letter: ")
    #print(f"the lower letter for {char} is {lower(char)}")
    ascii_value = ord(char)
    lower_ascii_value = ascii_value + 32
    lower_char = chr(lower_ascii_value)
    print(f"The lower letter for {char} is {lower_char}")

def q10():# gets one char and prints the real char represented by the char
    char = input("Enter one char: " )
    print(f"The real character for {char} is {chr(ord(char)-3)} ")



def main():
    #  q1()
    #  q2()
    #  q3()
    #  q4()
    #  q5()
    #  q6()
    #  q7()
    #  q8()
    q9()
      #q10()
    
    



if __name__ == '__main__':
    main()
    
