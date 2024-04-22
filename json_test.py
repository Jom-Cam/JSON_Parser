import sys 

holder = " "

def index_char_check(self):
    print(self)
        



if len(sys.argv) != 2:
    print("Usage: python script.py <json_data>")
    sys.exit(1)

json_data = sys.argv[1]

print(f"You are using the data set '{json_data}'")

with open(json_data, 'r') as file:
    test_file = file.read()

# test_file = open("test.json").read()

try:
    if test_file[0] == '{' and test_file[len(test_file)-1] == '}':
        print("Stringyfy json")
        for position in test_file: 
            if position != '"' or position != ' ' or position != '{' or position != '}':
                holder += position
        print(holder)
        print(type(holder))
    else:
        print("0")
        print(f'this is the file used {test_file}')
        index_char_check(test_file)
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
except: 
    print("Invalid data sets")
    print("0")

# fail testing, does not work when a space is added in the end of the json file, improvements required. 
# Possible uses of while true loops, iterate through index and check per text, trigger unpon reaching a spesific character. e.g when reaching " start reading until end of " then carry on to iterate until : the loop again above, if } end, if , carry on.
 