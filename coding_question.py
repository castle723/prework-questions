def hello_name(user_name):
    print("hello_" + user_name + "!")

def first_odds():
    for number in range(1, 101, 2):
        print(number)

def max_num_in_list(a_list):
    return max(a_list)

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False
    
def is_consecutive(a_list):
 
    if len(a_list) <= 1:
        return True

    for i in range(1, len(a_list)):
        if a_list[i] != a_list[i - 1] + 1:
            return False

    return True