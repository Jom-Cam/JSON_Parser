import sys 

holder = " " 

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
            if position != '"' or ' ' or '{' or '}':
                holder += position
        print(holder)
        print(type(holder))
    else:
        print("0")
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
except: 
    print("Invalid data set(s)")
    print("0")