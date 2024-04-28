test_string = "{this is a test string : for manipulation practice}"

# looping through string printing each one: 
# for test in test_string:
#     print(test)

# printing only vowels: 
# for test in test_string:
#     if test == 'a' or test == 'e' or test == 'i' or test == 'o' or test == 'u':
#         print(test)

# looping until : 
# toggle = True

# for test in test_string:
#     while toggle:
#         if test == ':': 
#             toggle = False
#         else: 
#             print(test)
#             break

# creating a match finding function 

# first_check = False

# def index_check(string, x): 
#     for index in string: 
#         if index == x: 
#             return True
#         else: 
#            return False

# toggle = index_check(test_string, '{')
# print(toggle)

test_string_2 = '{ "a" : "b"    ewewewe'
holder = " "
current_index = 0

def index_check(string, x):  
    if string[current_index] != x:
        raise ValueError("Invalid JSON")
    current_index += 1

while current_index < len(test_string_2):
    try: 
        if test_string_2[current_index] == '{':
            print('start JSON')

        if test_string_2[current_index] == '}':
            print('end JSON')
            break
       
        print(f'this is current index of {current_index} and a character of {test_string_2[current_index]}')
    except:
        print('excepted')
    # print(test_string_2[current_index])
    current_index += 1

# Next step to use comparisons to cycle through string and compare as iterating through, using 'for loops inside' 'while loops' along with 'break' caluses toggoling true or false triggers.