
def q11():# gets one word and prints the represent print for Python
    word = input("Enter word: ")
    print(f"The represent print for Python is {word.rjust(10,'*')}")


def q12():# gets one num and prints the represent print for Python
    num_str = input("Enter one num: ")
    print(f"The represent print for Python is {num_str.rjust(10,'0')}")

def q13():# gets the distance of a trip and the amount of suitcases and prints the total price of the trip
    disrance = float(input("Enter the distance of the trip: "))
    amount_of_suitcases = float(input("Enter the amount of the suitcases: "))
    start_price = 15.2
    price_for_each_km = 1.9
    price_for_each_suitcases = 7.0
    total_price = start_price + price_for_each_km * disrance + price_for_each_suitcases * amount_of_suitcases
    print(f"distance = {disrance}, amount_of_suitcase = {amount_of_suitcases}, price = {total_price}")


def q14():# gets the wanted floor, start floor and now position of the elevator and prints the total time to reach the wanted floor
    wanted_floor = int(input("Which floor you want to go: "))
    start_floor = int(input("Which floor you started from: "))
    now_position = int(input("Which floor the elevator now: "))
    time_at_stop = 5
    time_between_floors = 3
    total_time = abs(now_position-start_floor) * time_between_floors + 2 * time_at_stop + abs(wanted_floor - start_floor) * time_between_floors
    print(f"The total time is {total_time} seconds")
      
def q15():# gets length and width of a rectangle and swaps them
    length = int(input("Enter the legnth of the ractangle: "))
    width = int(input("Enter the width of the ractangle: "))
    temp = length
    length = width
    width = temp
    print(f"length = {length}, width = {width}")
     
     
   
def main():
    #q11()
    #q12()
    q13()
    #q14()
    #q15()



if __name__ == '__main__':
    main()
    