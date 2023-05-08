
import os, sys
import binascii




# Get the directory of the current Python script
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

with open(script_dir + '\\testfile.pdf', 'rb') as f:
    binary_data = f.read()

#string_data = binary_data.decode('utf-8', errors='ignore')
string_data = binary_data.decode('utf-8', errors='replace')
print(string_data)
