import sys


def main(filepath):
    result = 0
    
    with open(filepath) as f:
        line = f.readline()
        if line != '':
            
            current_floor = 0
            
            for c in line:
                result += 1

                if c == '(':
                    current_floor += 1
                elif c == ')':
                    current_floor -= 1

                if current_floor == -1:
                    break

    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")