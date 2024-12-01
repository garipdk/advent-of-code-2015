import sys
import hashlib

def main(key_string):
    h = hashlib.new('md5')
    
    current_number = 1
    current_key = key_string + str(current_number)
    h.update(current_key.encode('ascii'))
        
    while not h.hexdigest().startswith("000000"):
        h = hashlib.new('md5')
        current_number += 1
        current_key = key_string + str(current_number)
        h.update(current_key.encode('ascii'))
    
    return current_number
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input key_string")