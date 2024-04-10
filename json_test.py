test_file = open("test.json").read()

if test_file[0] == '{' and test_file[len(test_file)-1] == '}':
    print("1")
else:
    print("0")

