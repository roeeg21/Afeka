def q13():
    word = input("Enter a word: ")
    empty = " "
    print(f"Is word {word} valid? {word is not empty and "a" in word}")

def q14():
    word1 = input("Enter a word: ")
    word2 = input("Enter a word: ")
    empty = " "
    not_empty = word1 is not empty and  word2 is not empty
    a_in_words = ("a" in word1) or ("a" in word2)
    print(f"does {word1} and {word2} meet the requirement? {not_empty and a_in_words}")

def q15():
    num = input("Enter a number: ")
    print(f"Is number {num} decimal? {"." in num}")

def q16():
    is_sunny = input("Is sunny day: ")
    tempture  = float(input("What is the tempture outside: "))
    print(f"Is it a good day for picnic? {tempture < 27 and is_sunny == True}")

def q17():
    attendacne = int(input("What is the precent of attendacne?"))
    submittes_works  = int(input("What is the precent of submittes_works? "))
    submit_work5 = input("Is the student submited work num 5? ")
    print(f"can student participate the exam? {attendacne >= 80 and submittes_works >= 70 and submit_work5 == True}")

def q18():
    amount_of_fruit = int(input("How many fruit did u buy?"))
    apples_price  = float(input("What is the price of apples? "))
    orenges_price = float(input("Is the price of orenges? "))
    print(f"Does customer gets a discount? {amount_of_fruit > 10 or apples_price == orenges_price}")

def q19():
    grade = int(input("What is the grade of the student? "))
    print(f"Does student gets a bonus? {grade >= 75 and grade <= 90}")


def q20():
    oop_python_course  = float(input("What is the price of apples? "))
    grade_computer_science = float(input("Is the price of orenges? "))
    print(f"Is a student eligible to enroll in an OOP Java course? {oop_python_course == False or grade_computer_science > 55}")
    



    







def main():
    q14()



if __name__ == '__main__':
    main()