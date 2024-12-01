import sys


def main(filepath):
    result = 0
    
    with open(filepath) as f:
        line1 = f.readline()
        if line1 != '':
            f.seek(0)
            
            for line in f:
                dimentions = line.split('x')
                if len(dimentions) == 3:
                    l = int(dimentions[0])
                    w = int(dimentions[1])
                    h = int(dimentions[2])
                    
                    min1 = min(l, w, h)
                    
                    min2 = 0
                    
                    if min1 == l:
                        min2 = min(w, h)
                    elif min1 == w:
                        min2 = min(l, h)
                    elif min1 == h:
                        min2 = min(l, w)
                    
                    result += (2 * (min1 + min2) + l*w*h)
    
    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")