import sys


def main(filepath):
    result = 0
    
    with open(filepath) as f:
        line = f.readline()
        if line != '':
            num_parenthesis_open = line.count('(')
            num_parenthesis_close = line.count(')')
            
            result = num_parenthesis_open - num_parenthesis_close

    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")