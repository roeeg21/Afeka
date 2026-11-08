def q13():
    word = input("Enter a word: ")
    empty = ""
    letter_a = 'a'
    print(f"Is word {word} valid? {word is not empty and letter_a in word}")

def q14():
    word1 = input("Enter a word: ")
    word2 = input("Enter a word: ")
    empty = ""
    letter_a = 'a'
    not_empty = word1 is not empty and  word2 is not empty
    a_in_words = (letter_a in word1) or (letter_a in word2)
    print(f"does {word1} and {word2} meet the requirement? {not_empty and a_in_words}")

def q15():
    num = input("Enter a number: ")
    print(f"Is number {num} decimal? {"." in num}")

def q16():
    is_sunny = input("Is sunny day (True/False): ")
    tempture  = float(input("What is the tempture outside: "))
    max_ttempture = 27
    print(f"Is it a good day for picnic? {tempture < max_ttempture and bool(is_sunny) == True}")

def q17():
    attendacne = int(input("What is the precent of attendacne?"))
    submittes_works  = int(input("What is the precent of submittes_works? "))
    submit_work5 = input("Is the student submited work num 5? ")
    min_precent_of_submittes_works = 70
    min_precent_of_attendacne = 80
    print(f"can student participate the exam? {attendacne >= min_precent_of_attendacne and submittes_works >= min_precent_of_submittes_works and bool(submit_work5) == True}")

def q18():
    amount_of_fruit = int(input("How many fruit did u buy?"))
    apples_price  = float(input("What is the price of apples? "))
    orenges_price = float(input("Is the price of orenges? "))
    min_fruits = 10
    print(f"Does customer gets a discount? {amount_of_fruit > min_fruits or apples_price == orenges_price}")

def q19():
    grade = int(input("What is the grade of the student? "))
    min_grade = 75
    max_grade = 90
    print(f"Does student gets a bonus? {grade >= min_grade and grade <= max_grade}")


def q20():
    oop_python_course  = bool(input("Did you take OOP Python (True/False)? "))
    grade_computer_science = float(input("Enter Introduction to Computer Science grade: "))
    min_grade = 55
    print(f"Is a student eligible to enroll in an OOP Java course? {oop_python_course == False or grade_computer_science > min_grade}")
    


 
    







def main():
    q14()



if __name__ == '__main__':
    main()